H=list(input())
H[::2],H[1::2]=H[1::2],H[::2]
print(*H,sep="");
