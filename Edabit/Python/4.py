n=int(input("enter number :"))
i=0
for a in range(1,n+1):
    i+=a
    if a==3:
        continue
    print(a)