#
# Positional Arguments
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
    
# Calling the function with positional arguments
greet("Alice", 25) # output: Hello Alice, you are 25 years old.

greet(25, "Alice")  # Incorrect order
# Output: Hello 25, you are Alice years old.


#
# Keyword Arguments
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
    
# Calling the function with keyword arguments
greet(age=25, name="Alice") # output: Hello Alice, you are 25 years old.

greet("Alice", age=25)  # Valid
# greet(age=25, "Alice")  # Invalid - Positional arguments must come first


#
# Default Arguments and Default Parameter Value
def greet(name, age=18):  # Default value for 'age'
    print(f"Hello {name}, you are {age} years old.")
    
# Calling the function with and without the default argument
# Uses the default value for 'age'
greet("Alice") # Hello Alice, you are 18 years old.

# Overrides the default value
greet("Bob", 30)  # Hello Bob, you are 30 years old.      

# Invalid example
# def greet(age=18, name):  # SyntaxError: non-default argument follows default argument


#
# Arbitrary Arguments (*args)
def sum_numbers(*args):
    total = sum(args)
    print(f"The sum is: {total}")
    
# Calling the function with different numbers of arguments
sum_numbers(1, 2, 3) # output: The sum is: 6
sum_numbers(10, 20, 30, 40) # output: The sum is: 100


#
# Arbitrary Keyword Arguments (**kwargs)
def display_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
# Calling the function with different keyword arguments
display_user_info(name="Alice", age=25, location="New York")
display_user_info(name="Bob", profession="Developer")
''' output ->
name: Alice
age: 25
location: New York
name: Bob
profession: Developer
'''


#
# Combining *args and **kwargs
def mixed_arguments(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# Calling the function with both types of arguments
mixed_arguments(1, 2, 3, name="Alice", age=25)
'''output ->
Positional arguments: (1, 2, 3)
Keyword arguments: {'name': 'Alice', 'age': 25}
'''
