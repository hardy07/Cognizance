#2. Multiplying a matrix using numpy
import numpy as np  #importing numpy
first=np.array([[1,2,3],[4,5,6],[7,8,9]])  #first matrix
print("First matrix:")
print(first)
secnd=np.array([[4,2,0],[9,1,1],[6,9,6]])  #second matrix
print("Second Matrix:")
print(secnd)
res=np.multiply(first,secnd)  #used np.multiply() to multiply both the arrays 
print("Multiplication of the two matrices are:")
print(res)

#5.Array re-dimensioning using numpy
a = np.array([9, 1, 1, 4, 2, 0, 6, 9, 6, 1, 2, 3])
print("\nBefore re-dimensioning:")
print(a)
newa = a.reshape(4, 3) #reshape() gives a new shape to an array
print("After re-dimensioning:")
print(newa)
