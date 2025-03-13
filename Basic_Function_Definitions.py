#!/usr/local/bin/python3


# A Function Without Parameters:
def greet():
    print("Hello! Welcome to Python programming.")
    
# Calling the function
greet() #output -> Hello! Welcome to Python programming.


# A Function With Parameters
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python programming.")
    
# Calling the function with an argument
greet_user("Alice") # output -> Hello, Alice! Welcome to Python programming.


# A Function That Returns a Value
def add_numbers(a, b):
    return a + b

# Calling the function and storing the result
result = add_numbers(10, 20)
print(f"The sum is: {result}") # output -> The sum is: 30


# Function definition
def say_hello(name):
    print(f"Hello, {name}!")

# Function call
say_hello("John")
