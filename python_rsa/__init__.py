# Not the fastest method!

import math


def generate_Pk_and_pk(p, q):

    # Compute n and t
    n = p * q
    t = (p - 1) * (q - 1)
    
    # Compute e
    e = 2
    while e > 1 and e < t:
    
        if math.gcd(e, t) == 1:
        
            break
            
        else:
        
            e += 1
            
    # Compute d
    d = 2
    while True:
    
        if (d * e) % t == 1:
        
            break
            
        else:
        
            d += 1
          
    # Make key pairs
    Pk = (e, n)
    pk = (d, n)
    
    return(Pk, pk)
    
    
def encrypt(m, Pk):

    e, n = Pk

    if m > n:
    
        raise ValueError("m is greater than n")

    return((m ** e) % n)


def decrypt(c, pk):

    d, n = pk
    
    return((c ** d) % n)
    
    
    
    
    
    
    
    
    
    
