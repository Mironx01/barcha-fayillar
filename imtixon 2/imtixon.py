# n=int(input('n='))
# if n%4==0:
#     s=n/2
#     print(s,'quloqlar soni')
# else:
#     print('sanashda adashgan')    

# x=int(input('x='))
# y=int(input('y='))
# z=int(input('z='))
# if x<z and y>z:
#     print(z,'x va y oraliqida')
# else:
#     print('bu oraliqda emas')    


# n=30
# s=0
# for i in range(1,n+1):
#     if i%3==0:
#         s=s+i
# print(s)    



# n=int(input('n='))
# s=0
# for i in range(10,n+1):
#     s=s+i
# print(s)    
import math
n=int(input('n='))
s=0
for i in range(1,n+1):
    s=s+1/i**2
print(s)