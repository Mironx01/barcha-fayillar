# n=int(input('n='))
# for i  in range(1,n+1):
#     if n%i==0:
#         print(i)


# n=int(input('n='))
# s=0
# for i in range(1,n+1):
#     if n%i==0:
#         s=s+i
# print(s)


# n=int(input('n='))
# s=0
# for i in range(1,n):
#     if n%i==0:
#         s=s+i
# if s==n:
#     print('mukkammal son')
# else:
#     print('mukamal son emas')  



# n=int(input('n='))
# s=0
# for i in range(2,n+1):
#     for j  in range(1,i):
#         if i%j==0:
#             s=s+j
#     if s==i:
#         print(s)
#     s=0
#     j=1        


# n=int(input('n='))
# for i in range (1,n+1):
#     if i%3==0 and i%5!=0:
#         print(i)   


# n=int(input('n='))
# s=0
# for i in range(1 ,n+1):
#     if n%i==0:
#         s=s+1
# if s==2:
#     print('tub son') 
# else:
#     print('bu tub  son emas')   

# n=int(input('n='))
# s=0 
# for i in range(1,n):
#     for j in range(1,i+1):
#         if i%j==0:
#             s=s+1
#     if s==2:
#         print(j)
#     s=0   

# j=0    
# k=0
# l=0
# m=0
# for i  in range(0,7,1):
#     if i==1 : 
#         for j in range  (0,7,1):
#             if j==4:
#                 for k in range(0,7,1):
#                     if k==3:
#                         for l in range(0,7,1):
#                             if l==2:
#                                 for m in  range(0,7,1):
#                                     if m==2:
#                                         print(i,j,k,l,m)





# x=int(input('x='))
# y=int(input('y='))
# if x>y:
#     print(x, 'katta')
# elif y>x:
#     print(y,'katta')
# else:
#     print('ikklasi teng')


# x=int(input('x='))
# y=int(input('y='))
# z=int(input('z='))
# if x>y>z:
#     print(x)
# elif y>x>z:
#     print(y)
# elif z>x>y:
#     print(z)
# else:
#     print('ikkisi ham teng')         


n=int(input('n='))
s=0 
for i in range(1 ,n+1):
    for j in range(1,i+1):
        s=s+j
    if s==n:
        print(s,'bu mukkammal son')
    s=0



# n=int(input('n='))
# for i in range(1,n+1):
#     s=0
#     for j in range(1,i+1):
#         if i%j==0:
#             s=s+1
#     if s==2:
#         print(i)        


n=int(input('n='))
for i in range(1,n+1):
    s=0
    for  j in range(1,i+1):
        if i%j==0:
            s=s+1
    if s==2:
        print(i)    