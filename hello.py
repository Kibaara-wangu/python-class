def hello( name):
    print(f"hello {name}")

# two arguments
def year_of_birth(name,age):
    print(f"Hello {name}, you were born in {2024-age}")

# keyword argument and positional argument
    
def my_country(country="Uganda"):
    print(f"Hello AkiraChix from {country}") 


def greet( *names):
    for name in names:
     print(f"Hello{name}")


