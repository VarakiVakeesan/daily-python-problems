# You are given an integer N, reverse the digits of given number N, ensuring that the reversed number has no leading zeroes. Return the resulting reversed number.
def reverse_digit(n):
    length = len(str(n))-1
    res=0
    while length>=0:
        r = n%10
        res = res + (r*pow(10,length))
        length = length -1
        n=n/10
    return int(res)
N=int(input('Enter a number to reverse : '))
reversedNumber=reverse_digit(N)
print('Reversed Number of',N,'is',reversedNumber)