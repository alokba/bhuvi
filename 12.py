n=int(input("Enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print('*',end=" ")
    print()
for k in range(1,n):
    print(" "*k,end="")
    for m in range(1,n+1-k):
        print('*',end=" ")
    print()

n=int(input("Enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(n-j,end=" ")
    print()
for k in range(1,n):
    print(" "*k,end="")
    for m in range(1,n+1-k):
        print(n-m,end=" ")
    print()

n=int(input("Enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(0,i):
        print(n+j-i,end=" ")
    print()
for k in range(1,n):
    print(" "*k,end="")
    for m in range(1,n+1-k):
        print(m+k-1,end=" ")
    print()

n=int(input("Enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(0,i):
        print(chr(65+n+j-i),end=" ")
    print()
for k in range(1,n):
    print(" "*k,end="")
    for m in range(0,n-k):
        print(chr(65+k+m),end=" ")
    print()

n=int(input("Enter no. of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=" ")
    print()
for k in range(1,n):
    for m in range(1,n+1-k):
        print('*',end=" ")
    print()