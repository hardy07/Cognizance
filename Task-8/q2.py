#question2

import numpy as np #importing numpy
x = np.random.randint(1,8,6) #creating a random array as x and printing it
print("First array:\n", x)

y = np.random.randint(0,7,6) #creating a random array as y and printing it
print("Second array:\n", y)

equalornahh = np.allclose(x, y) #allclose() will check if both the arrays have similar elements are not and prints it as True or False
print(equalornahh)
