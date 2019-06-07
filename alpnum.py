x=input();
a=0
b=0
for i in x:
    if(i.isalpha()==True):
          a=a+1
    elif(i.isdigit()==True):
          b=b+1
if(a>=1 and b>=1):
    print("Yes")
else:
    print("No")
