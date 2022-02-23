numb=int(input("Enter a number:"))  # User input a int
temp=numb
rev=0

while(numb>0):  #while loop
    dig=numb%10
    rev=rev*10+dig
    numb=numb//10

if(temp==rev):  #if loop to verify if its a palindrome or not
    print("The number is palindrome!")
else:
    print("Not a palindrome!")




    