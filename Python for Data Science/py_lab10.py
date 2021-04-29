from numpy import *
'''
a = array([[1,2],[3,4],[5,6],[7,8]])
print(a.shape)
print(a.ndim)
print(a.size)
b=[len(i) for i in a]
print(b)
'''
'''
a = array([[11,22,33],[44,55,66],[77,88,99]])
print(a[:3,2:3])
'''
'''
a = array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]])
print(a[::2,1::2])
'''
'''
a=array([[34,43,73],[82,22,12],[53,94,66]])
print(a.max(axis=0))
print(a.min(axis=1))

'''



'''
def div(a,b):
  print(a/b)
  
def smart_div(func): // fun inside fun
  def inner(a,b):
    if a<b:
      a,b = b,a
    return func(a,b)
  return inner
  
div = smart_div(div)
div(2,4)
'''

'''
class computer:
  
  def __init__(self,name):
    self.name=name
    
  def config(self):
    print("A",self.name)
    
    
com1=computer("i5")
com1.config()
'''

'''
class student:
  def __init__(self,m1,m2):
    self.m1=m1
    self.m2=m2
    
  def __add__(self,other):
    m1=self.m1+other.m1
    m2=self.m2+other.m2
    s3=student(m1,m2)
    return s3
    
  def __gt__(self,other):
    r1=self.m1+self.m2
    r2=other.m1+other.m2
    if r1>r2:
      return True
    else:
      return False
      
  def __str__(self):
    return self.m1,self.m2
    
  def summ(self,a=None,b=None,c=None):
    s = 0
    if a!=None and b!=None and c!=None:
      s=a+b+c
    elif a!=None and b!=None:
      s=a+b
    else:
      s=a
      
    return s
    
    
s1=student(58,92)
s2=student(60,65)
s3=s1+s2
#print(s3)
if s1>s2:
  print("s1 wins")
else:
  print("s2 wins")
print(s1.summ(4,3,2))
'''
'''
class topten:
  def __init__(self):
    self.num=1
    
  def __iter__(self):
    return self
    
  def next(self): #__next__(self)
    if self.num<=10:
      val = self.num
      self.num += 1
      return val;
    else:
      raise StopIteration 
    
vals = topten()
for i in vals.items():
  print(i)
'''
'''
a=array([0,10,20,30])
b=array([0,2,4])
print(a[:,newaxis]+b)
'''

