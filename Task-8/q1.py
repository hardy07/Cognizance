#question1
import numpy as np #imported numpy

a= input("first number: ") #user input values for start point of the array
b= input("second number: ") #user input value for end point of the array
c=int(b)-int(a)+1
d=[]

for i in range(0,c): #make a for loop to print orginal array
    d.append(int(a)+i)
v=np.array(d) #orginal array made using loop 
print("Original array:\n", v) #printing the orginal array

p = int(input("Enter how many zeros to interleave in-between: ")) #user input for number of zeros to interleave in-between
new_num = np.zeros(len(v) + (len(v)-1)*(p))
new_num[::p+1] = v
print("New array:\n", new_num) #final array
