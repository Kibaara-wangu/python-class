# range
def print_numbers(n):
    numbers = range(n)
    for number in numbers:
        print(number)

# odd numbers
def print_odd_numbers(n):
    numbers = range(n)
    for number in numbers:
        if number % 2 !=0:
            print(number)

# even numbers
def print_even_numbers(n):
    numbers = range(n)
    for number in numbers:
        if number % 2 ==0:
            print(number)

# else statement
def odd_or_even(n):
    numbers = range(n)
    for number in numbers:
        if number % 2 ==0:
            print(f"{number} is even")
        else:
            print(f"{number} is not even")

# elif
def check_divisibility(n):
    numbers = range(n)
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} is divisible by 2")
        elif number % 3 == 0:
            print(f"{number} is divisible by 3")
        elif number % 5 == 0:
            print(f"{number} is divisible by 5")
        else:
            print(f"{number} is not divisible by 2,3 or 5")


def fizz_buzz(n):
    numbers = range(n)
    for number in numbers:
        if number % 3 == 0:
            print(f"fizz")
        elif number % 5 == 0:
            print(f"buzz")
        else:
            print("fizzbuzz")

# while loop
def count_down(n):
    while n > 0:
        print(n)
        n-=1           


def count_down_to_five(n):
    while n > 0:
        print(n)
        if n ==5:
            break
        n-=1

def divisile_by_seven(n):
    x = 0
    while x <= n:
        x+= 1
        if x % 7 != 0:
            continue
        print(f"{x} is divisile by 7")

def odd_numbers():
    num = 0
    while num <= 100:
         if num % 2 != 0:
             continue
         print(f"{num}is an odd number")
    num+=1


def fizz_buzz(n):
    numbers = range (n)
    for number in numbers:
         if number %3 ==0 and number %5 ==0:
             print("fizzbuzz")
         elif number % 3 == 0:
            print(f"fizz")
         elif number % 5 == 0:
            print(f"buzz")
         else:
            print(number)


fizz_buzz(100)

