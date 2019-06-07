n1,n2=input("").split()
n1=int(n1)
n2=int(n2)
for i in range(n1,n2):
     s=0
     t=i
     while(i!=0):
          r=i%10;
          s=s+r*r*r;
          i//=10;
     if(t==s):
        print(t,end=" ")
