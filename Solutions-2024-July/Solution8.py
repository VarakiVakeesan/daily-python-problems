# For a given number N check if it is prime or not. A prime number is a number which is only divisible by 1 and itself.
def isPrime (N)-> int:
    if (N==1 or N==0):
        return 0
    for i in range(2,int(pow(N,0.5))+1):
            if(N%i==0):
                return 0
    return 1
N=int(input('Enter an integer to find whether it is prime or not : '))
res=isPrime(N)
if res==0:
    print(N,"is not a prime number")
else:
    print(N,"is prime number")



