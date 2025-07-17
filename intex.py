# a="hello world"
# print(a[2])

# a="hello world"
# print(a[1:6])

# a="abcdefghijk"
# print(a[1:9:2])

# a="hello world"
# print(a[::-1])

# a="hello world"
# a[1]="y"
# print(a)

# a="hello world"
# print(a.upper())

# a="hello world"
# x=a.count("w")
# print(x)

# a='python is a fun programming language'
# print(a.find('fun'))

# a='hello world'
# x=a.replace('ll','dd')
# print(x)

# n=[21,22,23,24]
# print("before appand")
# print(n)
# print("after append")
# n.append(32)
# print(n)

# v=['a','e','i','u']
# v.insert(3,'o') ##insert 3 = 4 porstion
# print(v)

# n=[2,3,5]
# print(n)
# even=[4,6,8,2]
# print(even)
# n.extend(even)
# print(n)


# l=['py','sw','c++']
# l[2]='c'
# print(l)


# a=[1,2,3]
# n=int(input("enter no "))
# for i in range(0,n):
#     b=int(input("enter no to input"))
#     a.append(b)
# print(a)


# a=[]
# i=0
# n=int(input("enter no "))
# for i in range(0,n):
#     if(i%2==0):
#         a.append(i)
# print(a)

# v=['a','e','i','u','d','j','n']
# print(v[5::-1])


# prime_numbers = [2, 3, 5, 7]
# removed_element = prime_numbers.pop()
# print('Removed Element:', removed_element)
# print('Updated List:', prime_numbers)

# a=[1,2,3,4,5,6,7,8,9,10]
# e=[]
# o=[]
# for i in range(len(a)):
#     if i<=len(a)-1:
#         if(a[i]%2==0):
#             d=a.pop(i)
#             e.append(d)
#         else:
#             f=a.pop(i)
#             o.append(f)
# print("even=",e)
# print("odd=",o)

# a=[1,2,3,4,5,6,7,8,9,10]
# for i in range(len(a)):
#     if i<=len(a)-1:
#         if a[i]%2!=0:
#             a.pop(i)
# print("list=",a)




# f=[]
# while True:
#     print("1:add")
#     print('2.remove')
#     print("3.exit")
#     c=int(input("enter your choice"))
#     if(c==1):
#         a=int(input("enter a number:"))
#         f.append(a)
#         print(f)
#     if(c==2):
#         b=int(input("the number to remove"))
#         for i in range(len(f)):
#             if(i<len(f)-1):
#                 if(f[i]==b):
#                     f.pop(i)
#                     print(f)
#     if(c==3):
#         break



# l=["python","swift","c++","c","java"]
# # del l[1]
# # del l[-1]
# del l[0:2]
# print(l)

# l=["python","swift","c++","c","java"]
# l.remove("python")
# print(l)

# prime=[2,3,5,7,]
# prime.reverse()
# print(prime)

# l=[4,5]
# k=l*2
# print(k)

# l=[1,2]
# k=[3,4]
# m=l+k
# print(m)

# l=[1,2]
# a=len(l)
# print(a)

# l=[1,2]
# for i in l:
#     print(i)

# l=[1,2]
# print(3 in l)

# l=[1,2,3,33,4,10,6,5,]
# print(max(l))
# print(min(l))

# l=[1,2,5,3,4]
# k=[2,5,7,4,9,8]
# m=set(l).intersection(k)
# print(m)

# l=[1,2,5,3,4,2]
# k=[2,5,7,4,9,8]
# m=set(l) & set(k)
# print(m)

# l=[1,2,5,3,4]
# k=[2,5,7,4,9,8]
# g=[]
# for i in range(len(l)):
#         for j in range(len(k)):
#                 if(l[i]==k[j]):
#                     g.append(l[i])
# print(g)
# for i in l:
#     for j in k:
#          if(i==j):
#              g.append(i)
# print(g)


# l=[12,534,3,55]
# b=0
# for i in range(len(l)):
#     if l[i]>b:
#         b=l[i]
# print(b)
# c=l[0]
# for j in range(len(l)):
#     if (l[j]<c):
#         c=l[j]
# print(c)

# n=[1,2,3,4,5]
# a=[x**2 for x in n]
# print(a)

# matrix=[[j for j in range(3)]for i in range(3)]
# print(matrix)

# t=[0,1,2,3,4,5,6,]
# print(t)
# h=()
# print(h)
# m=("mouse",[5,5,6],[1,7,9])
# print(m)

# t=(0,1,2,3,4,5,6,)
# print(t[0])
# print(t[4])

# t=(0,1,5,3,4,5,6,)
# print(t[1:3])
# print(t[:-4])
# print(t[2:])
# print(t[:])

# t=(0,1,5)
# m=t*2
# print(m)

# t=(0,1,5,3,11,5,6,)
# print(t.count(5))
# print(t.index(11))

