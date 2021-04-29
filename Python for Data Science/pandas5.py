from pandas import *
from numpy import *
'''
name=['aparna','pankaj','sudhir','geeku']
degree=['mba','bca','m.tech','mba']
score=[90,78,80,98]

dict={'name':name,'degree':degree,'score':score}
df=DataFrame(dict)
df.to_csv("file.csv")


d=read_csv("file.csv")
df=DataFrame(d)
print(df)
'''
'''
name=['aparna','pankaj','sudhir','geeku']
degree=['mba','bca','m.tech','mba']
score=[90,78,80,98]

dict={'name':name,'degree':degree,'score':score}
df=DataFrame(dict)
df.to_csv("file1.csv",header=False,index=False)
#df.to_csv(r'C:\Users\Admin\Desktop\file2.csv')  #save at specific location

d=read_csv("file1.csv")
df=DataFrame(d)
print(df)
'''
'''
d=read_csv("stock.csv",squeeze=True)

def fun(num):
	if num<200:
		return "Low"
	elif num>=200 and num<400:
	    return "Normal"
    else:
    	return "High"
    	
    	
n=d.apply(fun)
print(n.head(10))
print(n.tail(10))
'''
'''
s=read_csv("stock.csv",squeeze=True)
n=s.apply(lambda num:num+10)
print(s.head(), '\n' ,n.head())
print(s.tail(), '\n' ,n.tail())
'''