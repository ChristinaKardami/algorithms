import argparse
import pprint
from collections import deque
parser = argparse.ArgumentParser()
parser.add_argument("-c","--connection", action="store_true")
parser.add_argument("-r", "--RADIUS",help="radius",type=int)
parser.add_argument("num_nodes",type=int, help="number of nodes")
parser.add_argument("file", help="the file")
args = parser.parse_args()
aktina=args.RADIUS
nloop=args.num_nodes
input_file=args.file
g = {}

with open(input_file) as graph_input:
    for line in graph_input:
        nodes = [int(x) for x in line.split()]
        if len(nodes) != 2:
            continue
        if nodes[0] not in g:
            g[nodes[0]] = []
        if nodes[1] not in g:
            g[nodes[1]] = []
        g[nodes[0]].append(nodes[1])
        g[nodes[1]].append(nodes[0])
if args.connection:
    for i in range(0,nloop):
        ma=-1 #max
        thesis=-1
        for k in g:
            n=len(g[k])
            if n > ma:
                ma=n 
                thesis=k
            elif n==ma:
                if k< thesis:
                    ma=n
                    thesis=k
        for k in g:
            for v in g[k]:
                if v==thesis:
                    g[k].remove(v)
        print(thesis, ma)
        del g[thesis]
else:
    
    def comboivasir(g, node, ra,aktina):
        length={}
        stop=True
        length[node]=0
        q = deque()
        visited = [ False for k in range(0,max(g)+1) ]#visited inque θεσεις οσες το μεγαλυτερο κλειδι του γραφου
        inqueue = [ False for k in range(0,max(g)+1) ]
        q.appendleft(node)
        inqueue[node] = True
        ball=[] #λίστα που κρτάει τους κόμβους είτε που βρίσκονται στη περιφέρειαα είτε βρίσκονται εντός της σφαίρας 
        while not (len(q) == 0) and stop:
            c = q.pop()
            inqueue[c] = False
            visited[c] = True
            for v in g[c]:
                if not visited[v] and not inqueue[v]:
                    mikos=length[c] + 1 #το μήκος του κόμβου είναι το μήκος του γονέα του αυξημένο κατα ένα
                    if mikos<=ra: #αν το μήκος ειναι μικροτερο ισο της ακτίνας ανήκει στην σφαίρα
                        length[v] = mikos #αρα το αποθηκευω στη λίστα με τα μήκη
                    else: #διαφορετικα
                        stop=False #σταματάω                   
                    q.appendleft(v)
                    inqueue[v] = True
        if ra == aktina: #αν η παράμετρος που έδωσε ο χρηστης ισούται με την ακτίνα
            for k in length: #για κάθε στοιχείο του λεξιλογίου που αποθηκέυω τα μήκη
                if length[k]==ra:
                    if k != node:
                     #αν το μήκος είναι ίσο με την ακτίνα, άρα ανήκει στη περιφέρεια
                        ball.append(k) #το προσθέτω στη λιστα ball
        else: #διαφορετικά αν θέλω να βρώ τους κόμβους που βρίσκονται εντος της σφαίρας, οπότε η παράμετρος είναι ακτίνα+1
            for k in length:
                if k != node:
                    ball.append(k) #προσθέτω στη λίστα όλους τους κόμβους
        return ball #lista me tous combous eite sti perifereia eite edws tis sferas
    tinfl={} #ορίζω ένα λεξικό

    def totalinfluence(g,aktina): #θέλω να βρώ την συνολική επιροή για τους κόμβους όλους του γράφου
        for c in g: #για κάθε κόμβο στον γάραφο
            comboi=comboivasir(g, c, aktina,aktina) #επέστρεψε τη λίστα των κόμβων που βρίσκονται στη περιφέρεια
            sum=0 
            for k in range(0,len(comboi)):#για κάθε θέση της λίστας που επιστρέφει τους κόμβους της περιφέρειας
                combos=comboi[k] #πάρε τη τιμή του  κόμβου
                n1=len(g[combos]) #βρές τον αριθμό των συνδέσμων του κόμβου
                n1=n1-1 #αφαίρεσε 1
                sum=sum+n1 #προσθεσε το στο συνολικό αθροισμα
            n2=len(g[c]) - 1 #βρες τον αριθμό των συνδέσμων του κόμβου που εηετάζει και αφαιρεσε 1
            influence= n2*sum #υπολόγισε τη συνολική επιρροή
            tinfl[c]=influence #κλειδί ο κόμβος που εξετάζω και τιμή η συνολική επιρροή
        return tinfl #επέστρεψε το λεξικό

    def maxinf(tinfl):
        max=-1
        thesis=-1
        for k in tinfl:
            
            n=tinfl[k]
            if n > max:
                max=n
                thesis=k
            elif n==max:
                if k< thesis:
                    max=n
                    thesis=k
        return thesis

    def changedinfluence(g,changedcomboi,aktina,tinfl):
        for element in changedcomboi:
            comboi=comboivasir(g, element, aktina,aktina) #επέστρεψε τη λίστα των κόμβων που βρίσκονται στη περιφέρεια
            sum=0 
            for k in range(0,len(comboi)):#για κάθε θέση της λίστας που επιστρέφει τους κόμβους της περιφέρειας
                combos=comboi[k] #πάρε τη τιμή του  κόμβου
                n1=len(g[combos]) #βρές τον αριθμό των συνδέσμων του κόμβου
                n1=n1-1 #αφαίρεσε 1
                sum=sum+n1 #προσθεσε το στο συνολικό αθροισμα
            n2=len(g[element]) - 1 #βρες τον αριθμό των συνδέσμων του κόμβου που εηετάζει και αφαιρεσε 1
            influence= n2*sum #υπολόγισε τη συνολική επιρροή
            del tinfl[element]
            tinfl[element]=influence #κλειδί ο κόμβος που εξετάζω και τιμή η συνολική επιρροή
        return tinfl #επέστρεψε το λεξικό

    z=totalinfluence(g,aktina)
    #pprint.pprint(z)
    totalinflu=totalinfluence(g,aktina)
    for i in range(0,nloop):
        #pprint.pprint(tinfl)
        combosmaxinfluence=maxinf(tinfl)
        print(combosmaxinfluence,totalinflu[combosmaxinfluence])
        rr=aktina+1
        changedcomboi=comboivasir(g,combosmaxinfluence,rr,aktina)
        for k in g:
            for v in g[k]:
                if v==combosmaxinfluence:
                    g[k].remove(v)
        del g[combosmaxinfluence]
        del tinfl[combosmaxinfluence]
        #print(changedcomboi)
        changedinfluence(g,changedcomboi,aktina,tinfl)
