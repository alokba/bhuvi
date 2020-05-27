n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i,i+1):
        print(i,end=" ")
        if i>=2:
           print(" "*(2*i-4),end="")
           for k in range(i,i+1):
              print(i,end=" ")
    print()

n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i,i+1):
        print(n+1-i,end=" ")
        if i>=2:
           print(" "*(2*i-4),end="")
           for k in range(i,i+1):
              print(n+1-i,end=" ")
    print()

n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i,i+1):
        print(chr(65+n-i),end=" ")
        if i>=2:
           print(" "*(2*i-4),end="")
           for k in range(i,i+1):
              print(chr(65+n-i),end=" ")
    print()

n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i,i+1):
        print(chr(64+i),end=" ")
        if i>=2:
           print(" "*(2*i-4),end="")
           for k in range(i,i+1):
              print(chr(64+i),end=" ")
    print()

n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(i-1),end="")
    for j in range(i,i+1):
        print("*",end=" ")
        if i<=4:
           print(" "*(2*n-2*i-2),end="")
           for k in range(i,i+1):
              print("*",end=" ")
    print()