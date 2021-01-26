import pprint
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--print", action="store_true")
parser.add_argument("n",help="number of polyomino",type=int)
args = parser.parse_args()
def graph(n):
    g = {}
    k=n
    for i in range(2-n, n):
        if i<=0:
            k = k-1
            if i == 0:
                l = 0
            else:
                l=1
        else:
            l = 0
            k = k+1
        z = n - abs(k) + 1
        for j in range(l, z):
            if i== -n+2:
                g[(i,j)]= (i+1,j)
            elif i == n-1:
                g[(i,j)]= (i-1,j)
            elif abs(i) + j == n-1:
                if i < 0:
                    g[(i,j)] = (i+1, j), (i, j-1)
                elif i==0: 
                    g[(i,j)] = (i,j-1)
                else:
                    g[(i,j)] = (i-1,j), (i, j-1)
            elif i == j and i == 0:
                g[(i,j)] = (i+1, j), (i, j+1)
            elif (i<0 and j==1) or j == 0:
                g[(i,j)] = (i+1,j), (i,j+1), (i-1, j)
            else:
                g[(i,j)] = (i+1, j), (i,j+1), (i-1,j), (i, j-1)  
    return g   
g=graph(args.n)         
if args.print:
    pprint.pprint(g)
untried={(0,0)}
class MyClass():
  x= 0
c= MyClass()
p = []
n=args.n
def FindIfNeighbor(v,pol,u,graph):
    for element in pol:
        if element !=u:
            if v in g[element]:
                return False
    return True
def CountFixedPolyominoes(g,untried,n,p,c):
    while untried:
        u =untried.pop()
        p.append(u)
        if len(p)== n:
            c.x=c.x+1
        else:
            new_neigh=set()
            for v in g[u]:
                if v not in untried and v not in p and FindIfNeighbor(v,p,u,g):
                    new_neigh.add(v)        
            new_untried=untried | new_neigh
            CountFixedPolyominoes(g,new_untried,n,p,c)
        p.remove(u)
    return(c.x)
CountFixedPolyominoes(g,untried,n,p,c)
print(c.x)
