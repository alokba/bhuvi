n=int(input("enter no.of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    for k in range(1,i):
        print(chr(64+k),end=" ")
    print()

n=int(input("enter no.of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(n+1-j,end=" ")
    print()

n=int(input("enter no.of rows:"))
for i in range(1,n+1):
    print(" "*(i-1),end="")
    for j in range(1,n+2-i):
        print('*',end=" ")
    for k in range(1,n+1-i):
        print("*",end=" ")
    print()

n=int(input("enter no.of rows:"))
for i in range(1,n+1):
    print(" "*(i-1),end="")
    for j in range(0,n+1-i):
        print(n+1-i,end=" ")
    for k in range(1,n+1-i):
        print(n+1-i,end=" ")
    print()


n=int(input("enter no.of rows:"))
for i in range(1,n+1):
    print(" "*(i-1),end="")
    for j in range(0,n+1-i):
        print(2*n+1-2*i,end=" ")
    for k in range(1,n+1-i):
        print(2*n+1-2*i,end=" ")
    print()