
# Example of Returning a Single Value:

def square(number):
    """Calculates and returns the square of a number."""
    result = number * number
    return result

squared_value = square(5)
print("The square of 5 is:", squared_value)  # Output: The square of 5 is: 25



# Returning Multiple Values
def divide_and_remainder(dividend, divisor):
    """Calculates and returns the quotient and remainder of a division."""
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

result_quotient, result_remainder = divide_and_remainder(10, 3)
print("Quotient:", result_quotient)  # Output: Quotient: 3
print("Remainder:", result_remainder)  # Output: Remainder: 1



# Returning Multiple Values as a Dictionary
# Returning a dictionary is beneficial when returning structured data with named keys.
def get_employee_details():
    """Returns employee details as a dictionary"""
    return {"name": "John", "age": 30, "department": "IT"}

employee = get_employee_details()
print(employee["name"])  # Output: John
print(employee["age"])   # Output: 30
print(employee["department"])  # Output: IT

