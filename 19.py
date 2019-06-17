A,B=map(int,input().split())
m=list();
for i in range(I,R+1):
  count=0
  for j in range(1,i+1):
      if(i%j==0):
         count+=1
  if(count==2):
        m.append(i) 
print(len(m));
