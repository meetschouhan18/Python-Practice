import numpy as np
import pandas as pd


# Creating Series
# 1. Using array
s = np.array([1,np.nan,'Panda'])
s1 = pd.Series(s)
print(s1)

# 2. Using List
li = ['Animal','2','lamina']
s2 = pd.Series(li)
print(s2)

# 3. Using Dictionary
s3 = pd.Series(
  {'Integer' : 3,
'B' : 'Boys'})
print(s3)


# Creating DataFrame

#when we join series together, we create a dataframe
# 1. Passing a numpy array
df = pd.DataFrame(np.random.randn(6,4))
print(df)

# 2. Using dictionary
df2 = pd.DataFrame({
  'A':1,
'number':np.array([6]*3,dtype='int32'),
})
print(df2)


# Importing/Exporting Data

# Import
df4 = pd.read_csv('path to the file(if file is present in system) or url')
print(df4.head(3)) #this will allow us to view 1st three lines of the csv file
#we can also import json files
df5 = pd.read_json('path to the file(if file is present in system) or url')
print(df5.head(3))
# .head(n) prints first n lines of the dataframe
# .tail(n) prints last n lines of the dataframe

#Export
file.to_json('path to the folder/name of file you want')
#similarly with csv
#ex - df4.to_csv('/home/Rohan/Desktop/file1.csv')


#Data Summary
#we have learned to import and export files
#now we learn how to summarize data
# we require a dataframe to work upon
#thus we take df2 for example

# Quick Summary
print(df2.info()) #this provide little information about our dataframe

# Detailed Summary
print(df2.describe()) #this tells each and every detail about our dataframe

# To view columns
print(df2.columns) #prints all columns

# Viewing Datatypes
print(df2.dtypes) #prints all types of data present in the dataframe

# Finding Duplicate row
print(df2.duplicated()) #this will provide boolean output of each row
#False means not duplicate
#True means duplicate

# Deleting Duplicate row
print(df2.drop_duplicates()) #this will delete duplicate rows from our dataframe

#Detecting Missing Value
print(df2.isnull().sum()) #this will provide int value of each row, telling the number of missing data in that row

#Drop Missing Value
print(df2.dropna()) #this will remove the rows with missing or null values


# Numeric Operations
# 1. Mean
print(df2.mean())

# 2. Cumulative Sum
print(df2.apply(np.cumsum)) # this will print total sum

#3. Max and Min value
print(df2.max())
print(df2.min())


#String Manipulation
# we need a series to work upon, thus s1 is taken as example
# Converting string to lowercase
print(s1.str.lower())

#Converting string to uppercase
print(s1.str.upper())

# Swap Capitalization
print(s1.str.swapcase()) #lower character becomes upper and vice versa

# Finding length of string
print(s1.str.len())

# Splitting String
print(s1.str.split()) #list of strings is created for each row

# Detecting Unique Value
print(s1.unique()) #this prints every unique value in the series in the form of an array

#Repeating String
s7 = np.array(['animal','bird',' Pandas Library '])
s7 = pd.Series(s7)
repeat_list = [2,3,5]
print(s7.str.repeat(repeat_list))
#in this the string present in row 0 is repeated 2 times
# string in row 1 is repeated 3 times
# string in row 2 is repeated 5 times

#
