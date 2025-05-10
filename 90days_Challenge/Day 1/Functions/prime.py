def prime(n):
    if (n<=1):
        return False
    else:
        for i in range(2,n+1):
            if(n%i==0):
                return False
        return True
n = int(input("Enter th number"))
if prime(n):
    print(f"{n} is prime number")
else:
    print(f"{n} is not a prime number")
