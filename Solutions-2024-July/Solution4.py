# You are given an integer N, reverse the digits of given number N, ensuring that the reversed number has no leading zeroes. Return the resulting reversed number.
def reverse_digit(n):
        res=0
        while n!=0:
            r = n%10
            res = res*10 + r
            n=n//10
        return res
N=int(input('Enter a number to reverse : '))
reversedNumber=reverse_digit(N)
print('Reversed Number of',N,'is',reversedNumber)