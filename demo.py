t = int(input(""))

while t>0:
    n = int(input())
    for i in range(n):
        if i==0:
            print("3",end = ' ')
        elif i%2==0:
            print(2*i,end = ' ')
        elif i%2==1:
            print(i*i,end = ' ')
    print('')
    t=t-1