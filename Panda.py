import pandas as pd

#printing data in a tabulated manner
animals = ['tiger', 'bear', 'moose']
print(pd.Series(animals))
numb = [1,2,3]
print(pd.Series(numb))
# since index is not mentioned, index is automatically generated
#this will also print data's type
a = pd.Series(['A','B','C'], index = ['a','b','c'])
print(a)
#index are inputted
sp = {'Cricket': 'India' , 'Football' : 'France' , 'Kabadi' : 'Iran'}
s = pd.Series(sp)
print(s)
#in case of dictionary keys becomes indexes and values becomes data


#printing index
print(s.index)

#Data selecting and projecting from DataFrame based on row and column labels

p_1 = pd.Series({'Name' : 'Chris' , 'Item Purchased' : 'Dog Food' , 'Cost' : 22.50})
p_2 = pd.Series({'Name' : 'Kevyn' , 'Item Purchased' : 'Kitty Litter' , 'Cost' : 2.50})
p_3 = pd.Series({'Name' : 'Vinod' , 'Item Purchased' : 'Bird Seed' , 'Cost' : 5.00})
# .Series creates a small table of the data specified
df = pd.DataFrame([p_1, p_2, p_3], index = ['Store 1', 'Store 2', 'Store 3'])

# .DataFrame creates table of multiple series
print(df.head(2)) # prints first 2 lines of the dataframe
print(df.tail(2)) # prints last 2 lines of the dataframe
#print(df.head()) or print(df.tail()) prints 5 lines of dataframe

# .loc does row selection
print(df.loc['Store 2']) # gives total details about the specified row
print(df['Item Purchased']) #gives specified column(i.e. Item Purchased in this case) for every row
print(df.T) #swap all columns and rows or transpose
# .loc can take 2 parameters i.e. row index and column name
print(df.loc['Store 2']['Cost'])

# .loc also support slicing
print(df.loc[:,['Name', 'Cost']]) #in this example we selected all rows and only 2 columns i.e. we removed the Item Purchased column

# .drop() is used to delete data and return a copy 
print(df.drop('Store 1'))
# data is not deleted from the actual table
print(df)

# .copy() is used to create a copy
copy_df = df.copy()
copy_df = copy_df.drop('Store 1')
print(copy_df)
# we can create another series using data from table
costs = df['Cost']
print(costs)
#but the problem is
#if we manipulate data in that sub-series then data is also changed in the original table from which sub-series was created
costs += 2
print(costs)
print(df)
# Thus copy function is useful

# another way to delete column
del copy_df['Name']
print(copy_df)

# we can add a row as follows
df['Location'] = None
print(df)

# Conditioning dataframe
print(df['Cost']>5) # Gives boolean result i.e condition is True or False for each row
print(df['Name'][df['Cost'] > 3]) #Name of those people who spend more than 3$ is printed

# .where - create a copy of the dataframe by putting NaN in the rows which does not satisfy the condition
df1 = df.where(df['Cost']>5)
print(df1)

# .dropna() is used to remove rows with NaN data
df1 = df1.dropna()
print(df1)

#Changing Index of Dataframe
df['Store'] = df.index #our index column has no title , so we give it one
df = df.set_index('Name') #Name column is now our index column
print(df)

# reset_index
df = df.reset_index() #remove index column and make a new simple index column(with index 0,1,2,3..)
print(df)

#multiple indexing
p_1 = pd.Series({'Name' : 'Chris' , 'Item Purchased' : 'Dog Food' , 'Cost' : 22.50})
p_2 = pd.Series({'Name' : 'Kevyn' , 'Item Purchased' : 'Kitty Litter' , 'Cost' : 2.50})
p_3 = pd.Series({'Name' : 'Vinod' , 'Item Purchased' : 'Bird Seed' , 'Cost' : 5.00})
df = pd.DataFrame([p_1, p_2, p_3], index = ['Store 1', 'Store 1', 'Store 2'])
df = df.set_index([df.index, 'Name']) # we setted indexes name and the one which is already the index
df.index.names = ['Location', 'Name'] # we named both indexes respectively
df = df.append(pd.Series(data={'Cost': 3.00, 'Item Purchased': 'Kitty Food'}, name=('Store 2', 'Kevyn'))) # we simply appended another data
print(df)
# name is the name of our index
# inside which there are 2 indexes, i.e. Location and Name respectively
