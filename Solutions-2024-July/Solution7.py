#Given an integer ‘N’, your task is to write a program that returns all the divisors of ‘N’ in ascending order.
N=int(input('Enter an interger to find divisors : '))
divisors=[1]
for i in range(2,N+1):
    if N%i==0 :
        divisors.append(i)
print('The divisors are : ',divisors)