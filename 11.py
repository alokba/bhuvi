n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(i-1),end="")
    for j in range(1,n+2-i):
        print(j,end=" ")
    for k in range(2,n+2-i):
        print(n+k-i,end=" ")
    print()

n=int(input("Enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(i-1),end="")
    for j in range(1,n+2-i):
        print(chr(65+n-i),end=" ")
    for k in range(2,n+2-i):
        print(chr(65+n-i),end=" ")
    print()

n=int(input("Enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(i-1),end="")
    for j in range(1,n+2-i):
        print(chr(65+2*n-2*i),end=" ")
    for k in range(2,n+2-i):
        print(chr(65+2*n-2*i),end=" ")
    print()

n=int(input("Enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(i-1),end="")
    for j in range(1,n+2-i):
        print(chr(64+j),end=" ")
    for k in range(2,n+2-i):
        print(chr(68+k-i),end=" ")
    print()

n=int(input("Enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for k in range(1,n):
    print(" "*k,end="")
    for l in range(1,n+1-k):
        print(l,end=" ")
    print()