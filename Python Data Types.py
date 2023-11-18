# -*- coding: utf-8 -*-
"""
Python Data Types
Spyder version 5.3.3
"""

# Import required libraries
import numpy as np
import pandas as pd

# This video will go over data types and their implications for multiple functions
# Some basic data types are boolean, integer and string
boolean_var = True

integer_var = 4

string_var = 'This is a string'

# The most basic function to understand data types is the type function
print(f"The types of these variables are: {type(boolean_var)}, {type(integer_var)}, {type(string_var)}")

# The data type also defines how some functions act. Booleans and integers do not have length for example
len(boolean_var)

len(integer_var)

len(string_var)

# Similarly, some values can have different data types, even if it is the same value
four_string = "4"

# If we compare both the four as an integer and the four as a string, we will notice that Python does not think they are the same
four_string == integer_var

# Even in numeric values, it can be very tricky. However, in the example below, 4.0 is equal to 4
float_four = float(4)

float_four == integer_var

# Values can be also converted from one data type to another using specific functions
integer_var == int(four_string)

# Lists and more complex objects also have data types
list_var = list((1, 2, 3, 4, 5))

type(list_var)

# For a list, the only way to check the data type of each instance is through iteration
# This is because lists can hold multiple data types
for var in list_var:
    print(type(var))
    
tuple_var = (2, 5, 7)   

type(tuple_var) 

for var in tuple_var:
    print(type(var))
# For dataframes, we have a different approach, as we can check every column
data = np.array([(1, 4, 6), (3, 5, 6), ('Flower', 'Tree', 'Nut')])
df = pd.DataFrame(data, columns = ['x', 'y', 'z'])


df

df.dtypes

# The object data type is used when you have multiple data types in a column, such as integers and strings here

# Let's create another dataframe to show it more clearly
data_2 = np.array([(1, 4, 6, 'Flower'), (3, 5, 6, 'Tree')])
df_2 = pd.DataFrame(data_2, columns = ['x', 'y', 'z', 'Label'])

# Check the data types again 
df_2.dtypes

# We can see how numpy convert them into objects by default, but we can change the data type
# The function astype allows us for a lot of flexibility on changing data types
# We are creating a copy of the column, and then reassigning it to the dataframe
df_2['x'] = df_2['x'].astype(int)

df_2['y'] = df_2['y'].astype(int)

df_2['z'] = df_2['z'].astype(int)

df_2['Label'] = df_2['Label'].astype(str)

# Now let's look at the data types again
df_2.dtypes

# Would would it happen if we try to convert the strings into text?
df_2['Label'].astype(int)

# Passing errors = 'ignore' will allow us to go through this limitation, but it will not do the transformation
df_2['Label'].astype(int, errors = 'ignore')

# Data types can be important if we want to filter by a numeric value, such as an integer
df_2['x'] > 2.1

# In this case Python correctly filters the data types needed, more so if we use this boolean subset
df_2[df_2['x'] > 2.1]

# As a final remark, there are other data types and kind of structures in Python. However, we will limit ourselves to these ones for now