#Given a positive integer N, determine whether it is odd or even.

def check_odd_or_even(N) :
    if N % 2 == 0:
        print(f"{N} is Even Number")
    else:
        print(f"{N} is Odd Number")

try:
    num = int(input('Enter a Positive Interger : '))
    check_odd_or_even(num)
except ValueError:
    print("Invalid input! Please enter a valid integer.")