n=int(input("Enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,2*i):
        print(i,end=" ")
    print()

#OR
n=int(input("Enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),(str(i)+" ")*(2*i-1))

n=int(input("Enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),(str(chr(64+i)+" "))*(2*i-1))

n=int(input("Enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),(str(chr(64+2*i-1)+" "))*(2*i-1))

n=int(input("Enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,2*i):
        print(j,end=" ")
    print()

n=int(input("Enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(2*i-1,0,-1):
        print(j,end=" ")
    print()