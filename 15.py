n=input()
f={}
for i  in n:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
p=max(f,key=f.get)
A=p;
print(A);
