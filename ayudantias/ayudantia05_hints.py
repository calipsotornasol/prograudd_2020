from collections import Counter

def dos_trios():
    a=[]
    L=mano()
    for e in L:
        aux=e.split()
        a.append(e[0])
    
    d=Counter(a) 
    
    print(d)
    
    cont=0
    
    for e in d.values():
        if e >=6:
            return 1
        
        elif e>=3:
            cont=cont+1
    
    if cont >=2:
        return 1
    else:
        return 0   