
# Passing Dictionaries as Arguments

# Example 1: Passing a Dictionary to a Function
def print_user_info(user):
    """Prints user details stored in a dictionary."""
    for key, value in user.items():
        print(f"{key}: {value}")

# Calling the function with a dictionary
user_data = {"name": "Alice", "age": 25, "location": "New York"}
print_user_info(user_data)

'''
output:
name: Alice
age: 25
location: New York
'''


# Example 2: Modifying a Dictionary Inside a Function
def update_user_info(user):
    """Adds a default role to the user dictionary."""
    user["role"] = "Member"

# Original dictionary
user_info = {"name": "Bob", "age": 30}

update_user_info(user_info)
print(user_info) # output: {'name': 'Bob', 'age': 30, 'role': 'Member'}



# Example 3: Preventing Modifications Using a Copy
def update_user_info(user):
    new_user = user.copy()  # Creates a copy of the dictionary
    new_user["role"] = "Member"
    return new_user

user_info = {"name": "Bob", "age": 30}
new_info = update_user_info(user_info)

print("Original Dictionary:", user_info) # output: Original Dictionary: {'name': 'Bob', 'age': 30}

print("Modified Dictionary:", new_info) # output: Modified Dictionary: {'name': 'Bob', 'age': 30, 'role': 'Member'}



