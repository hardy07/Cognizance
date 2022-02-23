num=int(input("Enter the number of rows: "))    # User input a string

for i in range(0,num):      #if loop
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()   #new Line

