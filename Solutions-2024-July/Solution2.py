#You are given two integer numbers, the base a and the index b. You have to find the last digit of a to the power of b.

a=int(input('Enter Valid Interger for Base:'))
b=int(input('Enter Valid Interger for Exponent:'))
print('First Method : ',int(pow(a,b) % 10))
print('Updated Method : ',pow(a,b,10))
