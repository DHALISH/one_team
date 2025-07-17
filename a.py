#a=10
#b=20

#print("a=",b)
#print("b=",a)

#b=a+b
#a=b-a
#b=b-a
#print (a)
#print(b)


#a,b=b,a
#print(a)
#print(b)


# print("a=",a,"b=",b)
# print("a={} b{}".format(a,b))
# print(f"a={a} b{b}")

# a="hgf"
# a=10
# print(type(a))

t="java"
l=0
for i in range(len(t)):
    for k in range(i):
        j=1
        if(t[i]==t[k] or t[k]!=l):
         print(t[k])
        j+=1
        l=l+t[k]
        print(j)