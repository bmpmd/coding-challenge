def ishex(s):
    if(len(s) > 6 ):
        return False 

    try:
        n = int(s,16)
        return True
    except ValueError:
        return False

print(ishex("CD5C5C"))
print(ishex("EAECEE"))
print(ishex("eaecee"))

print(ishex("CD5C58C"))# f 
print(ishex("CD5C5Z")) # f 

def isprime(n):
    return all(n % i for i in range(2, n))

def nextprime(n):
    # returns the next prime in range [n, 2n] 
     return min([a for a in range(n, 2*n) if isprime(a)])

print(nextprime(12)) # 13
print(nextprime(24)) # 29 
print(nextprime(11)) # 11 