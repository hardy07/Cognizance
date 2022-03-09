import pandas as pd #importing pandas
ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai' , 'campus'])
print(ser.str.capitalize()) #helps to convert the very first letter of given series in capital
