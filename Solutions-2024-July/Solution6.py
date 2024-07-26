#Given two positive integers a and b, find GCD of a and b.
def gcd(a : int, b : int) -> int:
        div=1
        if(a>b):
            a=b+a
            b=a-b
            a=a-b
        if b%a == 0:
            return a
        else:
            div=a//2
            while div>0:
                if a%div ==0:
                    if b%div ==0:
                        return div
                        break
                div=div-1
a=int(input('Enter one Positive integer : '))
b=int(input('Enter one Positive integer : '))
gcd1=gcd(a,b)
print('GCD of',a,b,'is',gcd1)