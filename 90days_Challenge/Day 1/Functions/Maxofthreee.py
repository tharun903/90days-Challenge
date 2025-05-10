def max(a,b,c):
    if(a>b):
        if(a>c):
            return a
        else:
            return c
    else:
        if(b>c):
            return b
        else:
            return c
a=int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the thrd number : "))
print(max(a,b,c))