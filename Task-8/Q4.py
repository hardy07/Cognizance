import pandas as pd # importing pandas
ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai' , 'campus'])
print(ser) #before capitalizing
print(ser.str.capitalize()) #After capitalizing
#Series.str.capitalize() helps to convert the very first letter of given series in capital
