from pandas import *
from numpy import *
'''
def main():
	d={'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]}
	df=DataFrame(d)
	print(df)
	
	df['add']=df.apply(sum,axis=1)
	print()
	print(df)

main()
'''
#options.mode.chained_assiganment=None
'''
def generate_range(n):
	n=int(n)
	ll=n//10 * 10;
	ul=ll+10
	return str(str(ll) + '-' + str(ul))
	
def replace(row):
	for i,item in enumerate(row):
		row[i]=generate_range(item)
		
	return row
	
def main():
	d={'A':[0,2,3],'B':[4,15,6],'C':[47,8,19]}
	df=DataFrame(d)
	print(df)
	
	df=df.apply(lambda row:replace(row))
	print(df)
	
main()
'''
'''
s=Series(['New york','Chicago','Toronto','Lisbon','Rio'])
i=[1,2,3,4,5]
s.index=i
print(s)
res=s.apply(lambda x:'Montreal' if x=='Rio' else x)
print(res)
'''
'''
df=read_csv("nba.csv")
print(df.aggregate(['sum','min']))
'''
'''
d={'Name':['Arjun','Karan','Harsh','Rakesh','Namit'],'Age':[19,20,20,21,19],'Department':['CS','EC','CS','IT','IT']}
d1={'Name':['Arjun','Harsh','Rakesh','Raman','Karan'],'Courses':['Machine Learning','OOPS','Web Development','OOPS','Data Structures']}

df=DataFrame(d)
df1=DataFrame(d1)

print(df)
print(df1)

inner_join=merge(df,df1,on='Name',how='inner')
print(inner_join)

outer_join=merge(df,df1,on='Name',how='outer')
print(outer_join)

left_join=merge(df,df1,on='Name',how='left')
print(left_join)

right_join=merge(df,df1,on='Name',how='right')
print(right_join)
'''


