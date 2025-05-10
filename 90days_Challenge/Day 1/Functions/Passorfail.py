def passorfail(a,b):
    if(a>35):
        print(f"{b} Passed the Exam with {a} Marks")
    else:
        print(f"{b} Failed the Exam with {a} Marks")

a=int(input("Enter the Marks : "))
b = input("Student name : ")
passorfail(a,b)