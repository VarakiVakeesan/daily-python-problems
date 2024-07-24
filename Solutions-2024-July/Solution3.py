#Given a number n. Count the number of digits in n which evenly divide n. Return an integer, total number of digits of n which divides n evenly.

def evenlyDivides (N):
        num=N
        count=0 
        # To store unique digits that evenly divide N
        unique_digits = set()
        while num!=0:
            r=num%10
            if r != 0 and N % r == 0:
                unique_digits.add(r)
                #count=count+1
            num=num//10
        #return count
        return len(unique_digits)

N=int(input('Enter a Positive Integer : '))
res = evenlyDivides(N)
print('number of digits in', N , 'which evenly divide',N ,'is : ', res)