n=int(input("n="))
i=1
s=0
j=1
while n>=j:
    while j>i:
        if j%i==0:
            s=s+i
        i=i+1 
    if s==j:
        print(s,"mukammmal son")    
    j=j+1