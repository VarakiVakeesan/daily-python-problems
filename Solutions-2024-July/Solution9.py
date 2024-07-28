# You are given a 3-digit number n, Find whether it is an Armstrong number or not.
n=int(input('Enter a three digit number : '))
sum=0
num=n
while n!=0 :
    r=n%10
    sum=sum+pow(r,3)
    n=n//10
if num==sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")