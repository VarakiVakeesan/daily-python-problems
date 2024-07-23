#Given a positive integer N, determine whether it is odd or even.

def check_odd_or_even(N) :
    if N % 2 == 0:
        print(f"{N} is Even Number")
    else:
        print(f"{N} is Odd Number")

while True:
    try:
        num = int(input('Enter a Positive Integer: '))
        if num <= 0:
            raise ValueError("The number is not positive.")
        check_odd_or_even(num)
        break  
    except ValueError as e:
        print(f"Invalid input! {e}")