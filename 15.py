n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(i-1),end=" ")
    for j in range(1,n+2-i):
        print("*",end=" ")
    print()

n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(i-1),end=" ")
    for j in range(1,n+2-i):
        print(n-i+1,end=" ")
    print()

n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(i-1),end=" ")
    for j in range(n+1-i,0,-1):
        print(j,end=" ")
    print()

n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(i-1),end=" ")
    for j in range(n+1-i):
        print(chr(65+n-i),end=" ")
    print()

n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(i-1),end=" ")
    for j in range(1,n+2-i):
        print(chr(65+n+1-i-j),end=" ")
    print()