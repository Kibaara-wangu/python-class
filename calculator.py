def add(a,b):
    answer = a+b
    return answer

def subtract(a,b):
    answer = a-b
    return answer

def multiply(a,b):
    answer = a*b
    return answer

def divide(a,b):
    answer = a/b
    return answer

def remainder(a,b):
    answer = a%b
    return answer

def power_of(a,b):
    answer = a**b
    return answer

def sum(* numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def multiply(* numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


def create_sentence(**words):
    print(words)
    sentence =" "
    for word in words.values():
        sentence += word
        sentence += " "
    return sentence

# def sum_and_greet(*args,**kwargs):
#     total = 0
#     for number in args:
#         total += number
#     greeting = f"Hello {kwargs["first_name"]} {kwargs["last_name"]}, the sum of {list(args)} is {total}"
#     return greeting


def sum_and_greet(*args,**kwargs):
    total = 0
    for number in args:
        total += number
        first_name=kwargs["first_name"]
        last_name=kwargs["last_name"]
        greeting=f"Hello {first_name} {last_name} the sum is {total}"
    return greeting



