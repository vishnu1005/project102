print("Automation Project")
intro =input("Enter 3 different items in storage:- ")
items=intro.split(',')
print(items)

ans=input("Do you want to keep "+items[0]+":- ")
print(items[0])

if  ans=="yes":
    print("Sure!")

else:
    del items[0]


ans1=input("Do you want to keep "+items[1]+":- ")
print(items[1])

if  ans1=="yes":
    print("Sure!")

else:
    del items[1]

ans2=input("Do you want to keep "+items[2]+":- ")
print(items[2])

if  ans2=="yes":
    print("Sure!")

else:
    del items[2]

print(items)



