def fibbonaci(n):
    a,b = 0,1
    series = []
    for i in range(n):
        series.append(a)
        a , b= b , a+b
    return series
n = int(input("Enter the number : "))
print(fibbonaci(n))