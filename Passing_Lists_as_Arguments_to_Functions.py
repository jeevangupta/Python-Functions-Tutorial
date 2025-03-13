
# Passing Lists as Arguments
# Example 1: Passing a List to a Function
def print_list_items(items): # This function iterates through the items and prints each item individually.
    """This function prints each item in the list."""
    for item in items:
        print(item)

# Calling the function with a list
fruits = ["Apple", "Banana", "Cherry"]
print_list_items(fruits)


# Example 2: Modifying a List Inside a Function
def modify_list(numbers):
    """This function multiplies each number by 2."""
    for i in range(len(numbers)):
        numbers[i] *= 2

# Original list
nums = [1, 2, 3, 4]
modify_list(nums)

print("Modified List:", nums) #output: Modified List: [2, 4, 6, 8]



# Example 3: Preventing Modifications Using a Copy
def modify_list(numbers):
    new_numbers = numbers[:]  # Creates a copy of the list
    for i in range(len(new_numbers)):
        new_numbers[i] *= 2
    return new_numbers

nums = [1, 2, 3, 4]
new_nums = modify_list(nums)

print("Original List:", nums) # output: Original List: [1, 2, 3, 4]

print("New List:", new_nums) # output: New List: [2, 4, 6, 8]
