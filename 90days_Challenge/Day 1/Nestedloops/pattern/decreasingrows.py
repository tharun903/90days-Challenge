w = int(input("Enter the rows : "))
# num = w
num = 1
for i in range(w,0,-1):
    # for j in range(1,i+1):
    #     print(num,end=" ")
    #     num-=1
    # print()
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()