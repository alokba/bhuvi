n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(i,end=" ")
    print()

n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()

n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()

n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()