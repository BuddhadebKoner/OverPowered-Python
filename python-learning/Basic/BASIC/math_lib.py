# write a python program to find
# power and squre root using user input.
import math

print('Enter number for calculating power of 2 nyumber')
a=int(input('enter first number: '))
b=int(input('enter power number: '))

c=math.pow(a,b)
print('power is =',c)

print('Enter number for calculating squreroot of a number')
d=int(input('enter the number: '))

e=math.sqrt(d)

print('squre root of',d,'is =',e)
