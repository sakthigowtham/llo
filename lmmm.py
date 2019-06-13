l=int(input());
l1=list(map(int,input().split()))
l1.sort(reverse=True)
for x in l1:
    print(x,end="")
