
n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(i-1),end=" ")
    for j in range(1,n+2-i):
        print(chr(64+j),end=" ")
    print()

n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for k in range(1,n):
    print(" "*k,end=" ")
    for l in range(1,n+1-k):
        print("*",end=" ")
    print()

n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(i,end=" ")
    print()
for k in range(1,n):
    print(" "*k,end=" ")
    for l in range(1,n+1-k):
        print(n-k,end=" ")
    print()

n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for k in range(1,n):
    print(" "*k,end=" ")
    for l in range(1,n+1-k):
        print(k+l,end=" ")
    print()

n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for k in range(1,n):
    print(" "*k,end=" ")
    for l in range(1,n+1-k):
        print(l,end=" ")
    print()