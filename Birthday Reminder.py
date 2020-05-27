dict={}
while True:
    print("------Birthday App------")
    print("1.Show Birthday")
    print("2.Add to Birthday List")
    print("3.Exit")
    choice=int(input("Enter the choice"))
    if choice==1:
        if len(dict.keys())==0:
            print("Nothing To Show")
        else:
            name=input("Enter to look for Birthday")
            birthday=dict.get(name,"No Data Found")
            print(birthday)
    elif choice==2:
        name = input("Enter a friend's Name")
        date = input("Enter Birthdate")
        dict[name]=date
        print("Birthday Added")
    elif choice==3:
        break
    else:
        print("Choose a valid option")