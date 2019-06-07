N = int(input())
a=input().split()
g=0
for i in range(len(a)):
 g=int(a[i])+g    
s=g//N
print(s)
