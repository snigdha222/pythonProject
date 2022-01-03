a = int(input('enter the number:'))
b=10
i=10
while i>0:

    if(a==b):
            print('the given number is equal to the taken number')
            break
    elif(a>b):
            print('select number which is less than now ')
            a = int(input('enter the number:'))
    else:
            print('select number which is greater than now')
            a = int(input('enter the number:'))
    i=i-1
print('you are out of the chances')