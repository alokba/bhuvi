n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(n-j,end=" ")
    print()
for k in range(1,n+1):
    for l in range(1,n+1-k):
        print(n-l,end=" ")
    print()

n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    for j in range(0,i):
        print(n+j-i,end=" ")
    print()
for a in range(1,n+1):
    for k in range(0,n-a):
        print(k+a,end=" ")
    print()

n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(65+n-i),end=" ")
    print()
for a in range(1,n+1):
    for k in range(0,n-a):
        print(chr(65+a),end=" ")
    print()

n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(65+n-j),end=" ")
    print()
for a in range(1,n+1):
    for k in range(n-a,0,-1):
        print(chr(64+k+a),end=" ")
    print()

n=int(input("enter no. of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+n-i+j),end=" ")
    print()
for a in range(1,n+1):
    for k in range(1,n-a+1):
        print(chr(64+k+a),end=" ")
    print()