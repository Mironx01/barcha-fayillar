n=int(input("n="))
i = 1
s = 0
while i <= n:
    if n%i==0:
        s=s+1
    i=i+1    
print("i=",i, "s=",s)
