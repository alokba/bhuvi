n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()
for k in range(1,n):
    print(" "*k,end=" ")
    for l in range(1,n+1-k):
        print(chr(64+n-k),end=" ")
    print()

n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()
for k in range(1,n):
    print(" "*k,end=" ")
    for l in range(1,n+1-k):
        print(chr(64+k+l),end=" ")
    print()

n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):  #forward printing 4 5
        print(n-i+j,end=" ")
    for k in range(2,i+1):  #backward printing 5 4 3 2
        print(n+1-k,end=" ")
    print()
for i in range(1,n+1):
    print(" "*i,end=" ")
    for j in range(i+1,n+1): #forward
        print(j,end=" ")
    for k in range(2,n+1-i): #backward
        print(n+1-k,end=" ")
    print()

n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(n+1-j,end=" ")
    for k in range(2,i+1):
        print(n-i+k,end=" ")
    print()
for i in range(1,n+1):
    print(" "*i,end=" ")
    for j in range(1,n+1-i): #forward
        print(n+1-j,end=" ")
    for k in range(2,n+1-i): #backward
        print(i+k,end=" ")
    print()

n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i,i+1):
        print("*",end=" ")
        if i>=2:
           print(" "*(2*i-4),end="")
           for k in range(i,i+1):
              print("*",end=" ")
    print()