import cmath
a=int(input('a value:'))
b=int(input('b value:'))
c=int(input('c value:'))
d=(b**2)-(4*a*c)
sq1=(-b-cmath.sqrt(d))/2*a
sq2=(-b+cmath.sqrt(d))/2*a
print(sq1)
print(sq2)