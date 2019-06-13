a=0
b=1
c=1
p=int(input())
for i in range(0,p):
    print(c,end=" ")
    c=a+b
    a=b
    b=c
    p=p-1
