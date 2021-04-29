from pandas import *
from numpy import *
'''
data = read_csv("nba.csv")
#data.dropna(inplace=True)
n=10
w=DataFrame(data["Weight"].head(n=n))
print(w.to_numpy())
'''
'''
data = read_csv("nba.csv")
#data.dropna(inplace=True)
n=10
w=Series(data["Weight"].head(n=n))
print(w.to_numpy())
'''
'''
s=Series(["dishen","dhruv","darshan","sharwil","rashesh"])
i=['1','2','3','4','5']
s.index=i
print(s)
#res=s.as_matrix()
#print(res)
'''
'''
d=read_csv("nba.csv")
n=10
print(d.head(n=n))
d.drop(["Team","Weight"],axis=1,inplace=True)
print(d.head(n=n))
'''
'''
d=read_csv("nba.csv",index_col="Name")
f=d.loc["Avery Bradley"]
s=d.loc["R.J. Hunter"]
print(f,"\n\n",s)
'''
'''
d=read_csv("nba.csv")
print(d.head())
nr=DataFrame({"Name":"dishen","Team":"bostan","Number":3,"Position":'PG',"Age":33,"Height":'6',"Weight":189,"College":'MIT',"Salary":10000},index=[0])
d=concat([nr,d]).reset_index(drop=True)
print(d.head())
'''
'''
d=read_csv("nba.csv",index_col="Name")
d.drop(["Avery Bradley"],inplace=True)
print(d.head())
'''