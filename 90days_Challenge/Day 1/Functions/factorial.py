def factorial(n):
    if(n==0) or (n==1):
        return 1
    else:
        return (n*factorial(n-1))
    
num = int(input("Enter the input : "))
if(num<0):
    print("Invalid")
else:
    print(factorial(num))