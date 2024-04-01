n=int(input("enter: "))

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n -1 )
    
print(fact(n))
a=int(input("enter number: "))
def prime(a):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

print(prime(n))