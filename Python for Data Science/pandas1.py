from numpy import *
from pandas import *
"""
a = array([1,2,3,4])
b = pd.Series(a)
print(b)

a = array([[1,2,3,4],[5,6,7,8]])
b = pd.DataFrame(a)
print(b)
"""
"""
from pandas import *
a = Series([1,2,3,4])
b = Series([5,6,7,8])
a=a.add(b)
print(a)
print(a.sort_values())
"""
'''
a = {'name':['tom','nick','krish','jack'],'age':[13,38,24,20],'birthdate':[4,31,20,11]}
df = DataFrame(a)
print(df[['name','birthdate']])
print(df['age'])
'''

# importing pandas module 
'''
import pandas as pd 
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv") 
data_top = data.head()
print(data_top)
'''
'''
import pandas as pd 
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv") 
n=9
s=data['Name']
top=s.head(n=n)
print(top)
'''

import pandas as pd 
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
n=10
data_bottom = data.tail(n=n) 
print(data_bottom)