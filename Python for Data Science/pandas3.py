'''import pandas as pd
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],'Height': [5.1, 6.2, 5.1, 5.2],'Qualification': ['Msc', 'MA', 'Msc', 'Msc']} 
df = pd.DataFrame(data) 

df.insert(1, "Age", [21, 23, 24, 21], True) 
print(df)

df=df.assign(address=['Delhi','Mumbai','Rajkot','Jamnager'])
print(df)

workplace={'Delhi','Banglor','Ahemdabad','Channei'}
df['Workplace']=workplace
print(df)
'''

from pandas import *
'''
d = read_csv("nba.csv",index_col="Name")
d.drop(['Avery Bradley','R.J. Hunter','John Holland'], inplace=True)
print(d.head())
'''
'''
d ={"A":[12, 4, 5, None, 1],"B":[7, 2, 54, 3, None],"C":[20, 16, 11, 3, 8],"D":[14, 3, None, 2, 6]}
df=DataFrame(d)
i = ['Row_1', 'Row_2', 'Row_3', 'Row_4', 'Row_5'] 
df.index = i
print(df)
res=df.truncate(before='Row_2',after='Row_4')
print(res)

sr=Series([19.5,16.8,22.78,20.12,18.10])
sr=sr.truncate(before=1,after=4)
print(sr)
'''
'''
d=read_csv("nba.csv",index_col="Name")
df=DataFrame(d.head())
for i,j in df.iterrows():
	print(i,"\n",j)
	print()
	
for key,value in df.iteritems():
	print(key,value)
	print()
	
for i in df.itertuples():
	print(i)
	
'''
'''
d=read_csv("employee.csv") #for null value
bool_series=isnull(d["Gender"])
print(d[bool_series])


d=read_csv("employee.csv") #not for null value
bool_series=notnull(d["Gender"])
print(d[bool_series])


d=read_csv("employee.csv")
d["Gender"].fillna("No Gender",inplace=True)
print(d)
'''
'''
from numpy import *
d=read_csv("employee.csv")
d.replace(to_replace=nan,value=-99)
print(d.head())
'''
'''
d=read_csv("employee.csv")
d=d.dropna(axis=0,how='any')
print(d)
'''
'''
d=read_csv("nba.csv")
d.sort_values("Name",axis=0,ascending=True,inplace=True,na_position='last')
print(d)
d.sort_values("Salary",axis=0,ascending=True,inplace=True,na_position='first')
n=50
print(d.head(n=n))
'''
'''
d=read_csv("nba.csv")
d.sort_values(["Team","Name"],axis=0,ascending=[True,False],inplace=True) #assending order of Team , descending order of Name
print(d.head())
'''