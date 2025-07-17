# Day1
# bag = ['Notebook', 'Pen', 'Charger', 'Lunchbox', 'Water bottle', 'ID card']
# current_contents = ['Pen', 'Water bottle'] 
# missing_items = [item for item in bag if item not in current_contents]
# if missing_items:
#     print("Don't forget to pack:", missing_items)
# else:
#     print("You're all set!")

# Day2
# - Start
# - Wake up
# - Freshen up (brush teeth, wash face)
# - Take a shower
# - Get dressed
# - Decide: "What’s for breakfast?"
# - Eat breakfast Pack bag
# - Check essentials (ID, keys, phone)
# - Lock door
# - Leave for work or school
# - End


# DAY3
# n=input("what is yorur name")
# a=int(input("how old are your"))
# print("hello,",n)
# print("you are",a,"old")

# DAY4
# a=int(input("enter the first number"))
# b=int(input("enter the second number"))
# if(a>b):
#     a+=10
#     print(a)
# else:
#     a-=10
#     print(a)

# DAY5
# n=input("enter yorur name")
# a=int(input("enter your age"))
# b=input("enter your favorite number")
# print("hello,",n,"you are",a,"years old your favorite number is",b)
                                                                                       #DAY6
                                                                                       #DAY7
# DAY8
# i=int(input("enter a number"))
# if(i>0):
#     print("number is postive")
# elif(i<0):
#     print("number is negative ")
# else:
#     print("number is zero")

# DAY9
# n=11
# t=0
# for i in range(1,11):
#     t+=i
# print(t)
#######
# a=[1,2,3,4,5,6]
# for i in range(0,7):
#     if(i%2==0):
#         print(i)


# DAY10
# while True:
#     n=input("enter the password")
#     if(n=="python123"):
#         print("correct password")
#         break
#     else:
#         print("enter the password correct ")
#######
# a=[1,2,3,4,5]
# if 6 in  a:
#     print("number found")
# else:
#      print("number not found")
#######
# secret=7
# max=3
# print("Guess the secret number between 1 and 10!")
# for i in range(1,max+1):
#     guess = int(input("Attempt {i}: Your guess? "))   
#     if guess == secret:
#         print("You guessed the secret number.")
#         break
# else:
#     print("Out of attempts!")



#DAY11
# r=4
# c=6
# for i in range(0,r+1):
#     for j in range(0,c+1):
#         print("*",end=" ")
#     print()
#######
# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         if(i==0 or i==4 or j==0 or j==4):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#######
# n=5
# for i in range(n,0,-1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()

#DAY15
# a=[]
# for i in range(0,5):
#     b=input("enter yor favorite food")
#     a.append(b)
# for j in range(0,5):
#     print("i love eating ",a[j])
                                                                                             #DAY16

# Day17
# t="Programming"
# print(t[0],t[-1])
# rt=t[::-1]
# print(rt)
# print(t.count("m"))
# y="Python is fun to learn"
# print(y.replace(" ","_"))
# x="madam"
# print(x==x[::-1])