count=1
a=-1
b=1
c=0
n=int(input('Enter the number of terms:'))
print('The fibonacci series is:')
while count<=n:
    c=a+b
    print(c)
    a=b
    b=c
    count=count+1
