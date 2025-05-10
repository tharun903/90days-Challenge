def palindrome(text):
    convert = text.lower().replace(" ","")
    
    return convert == convert[::-1]


s = input("Enter the text : ")
if(palindrome(s)):
    print("Its a palindrome")
else:
    print("Not a palindrome")