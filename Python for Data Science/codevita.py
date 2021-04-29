n = int(input()) 
'''five = int((n-4)/5)

if((n-5*five)%2==0): 
  one=2 
else: 
  one=1

two = (n-5*five-one)/2

print(one+two+five,five,two,one)'''
cnt=0
while n>=1:
  n = n/2; 
  cnt = cnt+1

print(cnt)