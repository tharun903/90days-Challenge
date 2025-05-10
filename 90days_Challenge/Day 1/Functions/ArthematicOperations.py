def add():
    print("Addition")
    print(a+b)

def sub():
    print("Subtraction")
    print(a-b)
def multiple():
    print("Multiplication")
    print(a*b)

c = (input("Enter Your choice :"))
a = int(input("Enter First Number : "))
b = int(input("Enter Seccond Number : "))

if(c=="Addition" or c=="addition" or c=="add"):
    add()
elif(c=="Subtraction" or c=="subtraction" or c=="sub"):
    sub()
elif(c=="Multiplocation" or c=="multiplocation" or c=="multiple" or c=="mul"):
    multiple()
else:
    print("Invalid input")
