import math
import argparse
import sys 
import random
parser = argparse.ArgumentParser()
parser.add_argument("-items", "--items", type=int, help="items")
parser.add_argument("-r","--radius", type=int,help="radius")
parser.add_argument("--min_radius","--MIN_RADIUS", type=int,help="min")
parser.add_argument("--max_radius","--MAX_RADIUS", type=int,help="max")
parser.add_argument("-b","--BOUNDARY_FILE",help="file" )
parser.add_argument("--seed","--seed", type=int,help="seeds")
parser.add_argument("output_file", help="the file")
args = parser.parse_args()

def orizodia_apostasi(mx,nx):
    dx=nx-mx
    return dx

def katheti_apostasi(ny,my):
    dy=ny-my
    return dy


def apostasi_kedrvn(dx,dy):
    temp= dx**2 + dy**2
    d=math.sqrt(temp)
    
    return d

def kedro_kuklou(rm,rn,r,d,dx,dy,mx,my):
    r1=rm+r
    r2=rn+r
    
    kx=0
    ky=0
    if d!=0:
        l=(r1**2 - r2**2 + d**2)/(2*d**2)
        
   
        e=(r1**2)/(d**2 )-( l**2)
        
        if e>=0:
            t=math.sqrt(e)
         
            x=mx+l*dx-t*dy
            y=my+l*dy+t*dx

            return round(x,2), round(y,2)
    
    return kx,ky

def apostasi_apo_euteia(ux,uy,vx,vy,cx,cy):
    l2=(ux-vx)**2 + (uy - vy)**2
    if l2==0:
        temp=(ux-cx)**2 + (uy-cy)**2
        d=math.sqrt(temp)
    else:
        t=((cx-ux)*(vx-ux) + (cy-uy)*(vy-uy))/l2
        px=ux+t*(vx-ux)
        py=uy+t*(vy-uy)
        temp=(px-cx)**2 + (py-cy)**2
        d=math.sqrt(temp)
    return round(d,2)

def kedro(circlelement):
    i=0
    for element in circlelement:
        if (i==0):
            x=element
        elif(i==1):
            y=element
        else:
            r=element
        i=i+1
    return x,y,r

def kodinoteroskuklos(mx,my):
    l=(mx)**2 + (my)**2
    d=math.sqrt(l)
    return round(d,2)

xek=0
yek=0
items=args.items
if(args.radius):
    r=args.radius
else:
    random.seed(args.seed)
    r=random.randint(args.min_radius,args.max_radius)
circle={}
circle[1]=[0,0,r]

if args.min_radius:
    r=random.randint(args.min_radius,args.max_radius)
circle[2]=[circle[1][2]+r,0,r]

metopo={}
metopo[1]=[2,2]
metopo[2]=[1,1]


for w in range(3,items +1):
    minimum=sys.maxsize
    loop=True
    
    
    for x in metopo.keys():            
        #if w!=3:
              
        cx,cy,cr=kedro(circle[x])
        
        apostasi=kodinoteroskuklos(cx,cy)
        #if w==13:
        #    print(x,apostasi)  σε αυτο το σημειο εμφανιζεται το προβλημα καθως η αποσταση του 6 κυκλου φαίνεται να ναι 16.99 ενω θα πρεπε να ειναι 17 
        #    αυτο συμβαινει διοτι σε ορισμενες συντεταγμένες προκυπτει λαθος στο δευτερο δεκαδικο κατα 0.01 λογικα λογω καποιου round
        if (apostasi<minimum):
            minimum=apostasi
            thesi=x
            Cm=circle[thesi]
        elif(apostasi==minimum):
            #if(w==13):
            #    print("hi")
            if(x<thesi):
                thesi=x
                Cm=circle[thesi]
        #if w==13:
        #    print(thesi)
    
    
    if args.min_radius:
            
        ri=random.randint(args.min_radius,args.max_radius)
    else:
        ri=args.radius
    
    while loop==True:    
        thesin=metopo[thesi][1]
        
        Cn=circle[thesin]
        #if w==13:
        #    print(thesi,thesin,metopo)
        mx,my,mr=kedro(Cm)
        nx,ny,nr=kedro(Cn)
        dx=orizodia_apostasi(mx,nx)
        dy=katheti_apostasi(ny,my)
        d=round(apostasi_kedrvn(dx,dy),2)
        tempx,tempy=kedro_kuklou(mr,nr,ri,d,dx,dy,mx,my)
        prostheto=True
        temneiepomenocn=False
        temneiproigcm=False
        elenxv=True
        stamatao=False

        #ΚΑΙΝΟΥΡΓΙΑΑΑ
        
        fores=len(metopo)//2
        ca=metopo[thesin][1]
        cb=metopo[thesin][0]
        i=0
        if ca!=cb or ca==cb:
            synexizv=True
            while synexizv==True and i<=fores:
                i=i+1
                xa,ya,ra=kedro(circle[ca])
                dkxa=orizodia_apostasi(xa,tempx)
                dkya=katheti_apostasi(tempy,ya)
                dka=round(apostasi_kedrvn(dkxa,dkya),2)
                xb,yb,rb=kedro(circle[cb])
                dkxb=orizodia_apostasi(xb,tempx)
                dkyb=katheti_apostasi(tempy,yb)
                dkb=round(apostasi_kedrvn(dkxb,dkyb),2)
                if(ri+ra > dka ):
                    thesicj=ca
                    temneiepomenocn=True
                    prostheto=False
                    break
                elif(ri+rb >dkb and cb!=thesi ):
                    thesicj=cb
                    temneiproigcm=True
                    prostheto=False
                    break
                
                if(temneiepomenocn==True or temneiproigcm==True ):
                    synexizv=False
                else:
                    ca=metopo[ca][1]
                    cb=metopo[cb][0]
               

        #if w==13:
        #    print(thesicj)



        if(prostheto==True):
            metopo[thesi][1]=w
            metopo[thesin][0]=w
            circle[w]=[tempx,tempy,ri]
            metopo[w]=[thesi,thesin]
            
            loop=False
        else:
            if temneiproigcm==True:
                g=thesicj
                frouros=metopo[thesin][0]
                g=metopo[g][1]
                y = metopo[g][1]
                while g!=thesin:#frouros:
                    del metopo[g]
                    g = y
                    y = metopo[g][1]
                    
                        
                    
                
                thesi=thesicj
                Cm=circle[thesi]
                mx,my,mr=kedro(Cm)
                metopo[thesi][1]=thesin
                metopo[thesin][0]=thesi
            elif temneiepomenocn==True:
                
                g=thesi
                g=metopo[g][1]
                y=metopo[g][1]
                while g!=thesicj:
                    del metopo[g]
                    g= y
                    y=metopo[g][1]
                    
                        
                thesin=thesicj
                Cn=circle[thesin]
                metopo[thesi][1]=thesin
                metopo[thesin][0]=thesi

with open(args.output_file,"w") as f:
    
    for i in circle:
        f.write(" ")
        xi,yi,ri=kedro(circle[i])
        f.write(str(xi ))
        f.write(" ")
        f.write(str(yi ))
        f.write(" ")
        f.write(str(ri ))
        f.write( "\n")
