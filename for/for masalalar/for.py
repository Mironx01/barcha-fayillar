# 9,1
# n=int(input('n='))
# for i in range(1,n+1):
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

#n=int(input('n=5'))    
from math import*

# n=int(input('n='))
# s1=sin(1)
# s2=1/sin(2)
# for i in range(2,n+1,1):
#     s1=s1+sin(i)
#     s2=s2+1/s1
# print(s2)

# n=int(input('n='))
# s1=cos(1)
# s2=sin(1)
# s=cos(1)/sin(1)
# for i in range(1,n+1,1):
#     s1=s1+cos(i)    
#     s2=s2+sin(i)
#     s=s+(s1/s2)
# print(s)    
 
 
# b= "hello, world!"
# print(b[2:5])

# b="Hello, World!"
# print(b[:5])
# b="Hello, World!"
# print(b[2:])
# a = "hello"

# b = "world"
# c=a + " " + b
# print(c)
# age = 36
# txt="my name is miron king"cjch9
# print(txt.format(age))
# quantity = 3
# itemno = 5000

# price = 49.95
# myorder = "i want to pay {,jki}"

# import random
# n=int(input('n='))
# s=0
# for i in range(0,n+1,1):
#     a=random.randint(1,n)
#     print(a)
#     s=s+a
# print(s)
import random
# n=int(input('n='))
# s=1
# for i in range(0,n+1,1):
#     a=random.randint(1,n)
#     print(a)
#     s=s*a
# print(s)

# import random
# n=int(input('n='))
# s=0
# for i in range(0,n+1,1):
#     a=random.randint(1,n)
#     print(a)
#     if a<0:
#         a*(-1)
#     s=s+a
# print(s)

import random
# n=int(input('n='))
# s=0
# for i in range(0,n+1,1):
#     a=random.randint(1,n)
#     print('tasodifiy son')
#     s=s+a
# print(s)
# a1=[]

# n=int(input('n='))
# s=0
# a1=[]
# p=1
# for i in range(0,n+1,1):
#     a=random.randint(1,n)
#     a1.append(a)
#     s=s+a
#     p=p*a
# print(a1,s,p)
# n=int(input('n='))
# s=0
# a1=[]
# p=1
# for i in range(0,n+1,1):
#     a=random.randint(1,n)
#     a1.append(a)
#     s=s+a**2
    
# print(a1,s,)
# n=int(input('n='))
# s=0
# a1=[]
# p=1
# for i in range(0,n+1,1):
#     a=random.randint(1,n)
#     a1.append(a)
# n=int(input('n='))
# s=0
# a1=[]
# for i in range(1 , n + 1):
#     z = random.randint(1 , n)
#     a1.append(z)
#     s = (-1 ** i) * z + s
# print(a1)
# print(s)









































































































































































































































































































































































































































































































































































#bu orqaga qoyadi
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

 #o'rtadan o'chirib tashlaydi
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# bu o'rniga qoyadi
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(0, "orange")
# print(thislist)

#bu ikkalasini qushadi
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# ikkta birxilni  1 chisini o'chiradi
# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)

# tanlangan predmetni o'chiradi
# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)

# bu yam pop day narsa
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

#o'chirib tashlaydi xammasini 
# thislist = ["apple", "banana", "cherry"]
# del thislist

# barcha elementlarni chop etadi
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)


# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

#whileBarcha indeks raqamlaridan o'tish uchun pastadir yordamida barcha elementlarni chop eting

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

# a harfi qatnashganlarini olib beradi
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)
#Faqat "olma"bo'lmagan narsalarni qabul qiling:
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if x != "apple"]

# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits]

# print(newlist)


# newlist = [x for x in range(10)]

# print(newlist)


# newlist = [x for x in range(10)]

# print(newlist)


# newlist = [x for x in range(10) if x < 5]

# print(newlist)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x.upper() for x in fruits]

# print(newlist)



# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = ['hello' for x in fruits]

# print(newlist)



# fruits = ["apple", "banana", "cherry", "kiwi", "orange"]

# newlist = [x if x != "banana" else "orange" for x in fruits]

# print(newlist)



#sort list


# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

# thislist.sort()

# print(thislist)



# thislist = [100, 50, 65, 82, 23]

# thislist.sort()

# print(thislist)


# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

# thislist.sort(reverse = True)

# print(thislist)


# thislist = [100, 50, 65, 82, 23]

# thislist.sort(reverse = True)

# print(thislist)


# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]

# thislist.sort(key = myfunc)

# print(thislist)



# thislist = ["banana", "Orange", "Kiwi", "cherry"]

# thislist.sort()

# print(thislist)


# thislist = ["banana", "Orange", "Kiwi", "cherry"]

# thislist.sort(key = str.lower)

# print(thislist)



# thislist = ["banana", "Orange", "Kiwi", "cherry"]

# thislist.reverse()

# print(thislist) 










#copy lists
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)


# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)


# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)


# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)










# append()          Ro'yxat oxirida element qo'shiladi
# clear()	        Ro'yxatdagi barcha elementlarni olib tashlaydi
# copy()	        Ro'yxatning nusxasini qaytaradi
# count()	        Belgilangan qiymat bilan elementlar sonini qaytaradi  
# extend()	        Joriy ro'yxatning oxiriga ro'yxat elementlarini (yoki har qanday takrorlanadigan) qo'shing      
# index()	        Belgilangan qiymat bilan birinchi elementning indeksini qaytaradi
# insert()	        Belgilangan holatda element qo'shadi
# pop()	            Belgilangan hoaltda elementni olib tashlaydi
# remove()	        Belgilangan qiymat bilan elementni olib tashlaydi
# reverse()	        Ro'xat tartibini o'zgartiradi
# sort()	        Ro'xatni tartiblaydi






































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































