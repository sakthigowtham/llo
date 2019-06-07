    
a,b=map(int,input().split())
c=list(map(int,input().split()))
q=0
for i in c:
  if(i==b):
    q=q+1
g=q
if (g!=0):
    print("yes")
else:
    print("no")
