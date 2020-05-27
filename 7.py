n=int(input("Enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(i-1),end="")
    for j in range(1,n+2-i):
        print((n+1-i),end="")
    print()

#OR
n=int(input("Enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(i-1),(str(n+1-i)*(n+1-i)))

n=int(input("Enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(i-1),end="")
    for j in range(1,n+2-i):
        print(j,end='')
    print()

n=int(input("Enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(i-1),(chr(65+n-i)*(n+1-i)))

n=int(input("Enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(i-1),end="")
    for j in range(1,n+2-i):
        print(chr(64+j),end="")
    print()

n=int(input("Enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),'*'*(2*i-1))

#OR
n=int(input("Enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,(2*i)):
        print("*",end="")
    print()