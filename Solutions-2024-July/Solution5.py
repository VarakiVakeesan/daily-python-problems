#Given two positive integers a and b, find GCD of a and b.
#using recursion - Euclidean algorithm

def gcd(a : int, b : int) -> int:
        # code here
        if(a>b):
            a=b+a
            b=a-b
            a=a-b
        if b%a==0:
            return a
        else:
            return gcd(b%a,a)

a=int(input('Enter one Positive integer : '))
b=int(input('Enter one Positive integer : '))
gcd1=gcd(a,b)
print('GCD of',a,b,'is',gcd1)