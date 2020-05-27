n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for i in range(1,2*i):
        print(chr(64+i),end=" ")
    print()

n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for i in range(2*i-1,0,-1):
        print(chr(64+i),end=" ")
    print()

n = int(input("enter no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i):     #reaching columns
        print(i-j,end=" ")   #printing only first element in each row
    for k in range(0,i):
        print(k,end=" ")     #printing rest of the elements in each row
    print()

n=int(input("enter no.of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i):
        print(chr(i-j+65),end=" ")
    for k in range(0,i):
        print(chr(65+k),end=" ")
    print()

n=int(input("enter no.of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(i-1,0,-1):
        print(k,end=" ")
    print()