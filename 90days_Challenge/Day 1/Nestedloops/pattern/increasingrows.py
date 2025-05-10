w = int(input("Enter the rows : "))
num = 1
for i in range(1,w+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()