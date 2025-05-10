def login(a,b):
    if(username==a and password==b):
        return "Login Successfull"
    else:
        return "Invalid Username or Password"
username = "Somu"
password = "Somu@123"

a = input("Enter Username : ")
b = input("Enter Password : ")
print(login(a,b))