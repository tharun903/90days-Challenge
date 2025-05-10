w = int(input("Enter the rows : "))
for i in range(w,0,-1):
    for j in range(i+1,0,-1):
        print(j,end=" ")
    print()
    # for j in range(0,i+1):
    #     print(j,end=" ")
    # print()