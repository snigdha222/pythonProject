n=153
temp=n
sum=0
while(n>0) :
    r=n%10
    sum=sum+(r**3)
    n=n/10
if (temp==sum):
    print('the value is armstrong')
else :
    print('the given value is not armstrong')