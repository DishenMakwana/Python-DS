from pandas import *
from numpy import *
'''
d={'Name':['jai','anuj','jai','princi','gaurav','anuj','princi','abhi'],'Age':[27,24,22,32,33,36,27,32]}
df = DataFrame(d) 
print(df)
df.groupby('Name')
print(df.groupby('Name').groups)
f=df.groupby('Name')
print(f.first())
'''
'''
d={'Name':['jai','anuj','jai','princi','gaurav','anuj','princi','abhi'],'Age':[27,24,22,32,33,36,27,32],}
df=DataFrame(d)
print(d)
df=df.groupby(['Name'],sort=True).sum()
print(df)
'''
'''

d={'Name':['jai','anuj','jai','princi','gaurav','anuj','princi','abhi'],'Age':[27,24,22,32,33,36,27,32],}
df=DataFrame(d)
grp=df.groupby(['Name','Age'])
for name,group in grp:
	print(name)
	print(group)
	print()
'''
'''
d={'Name':['jai','anuj','jai','princi','gaurav','anuj','princi','abhi'],'Age':[27,24,22,32,33,36,27,32],}
df=DataFrame(d)
grp=df.groupby('Name')
grp=grp.get_group('jai')
print(grp)
'''
'''
d={'Name':['jai','anuj','jai','princi','gaurav','anuj','princi','abhi'],'Age':[27,24,22,32,33,36,27,32],'Qualification':['msc','ma','mca','phd','b.tech','b.com','msc','ma']}
df=DataFrame(d)
grp=df.groupby('Name')
print(grp.aggregate(sum))
grp1=df.groupby(['Name','Qualification'])
print(grp1.aggregate(sum))
'''

'''
d={'Name':['jai','anuj','jai','princi','gaurav','anuj','princi','abhi'],'Age':[27,24,22,32,33,36,27,32],'Qualification':['msc','ma','mca','phd','b.tech','b.com','msc','ma'],'Score':[23,34,35,45,47,50,52,53]}
df=DataFrame(d)
grp=df.groupby('Name')
print(grp['Age'].agg([sum,mean,std]))

grp1=df.groupby('Name')
print(grp.filter(lambda x: len(x) >=2))
'''