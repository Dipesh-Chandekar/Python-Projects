"""
Sets and Functions
Write a function unique_elements(input_list) that takes a list as input and 
returns a set of unique elements from that list.
Example:
input_list = [1, 2, 2, 3, 4, 4, 5]
print(unique_elements(input_list)) # Output: {1, 2, 3, 4,
5}
"""

def unique_elements(list):
    return set(list)

if __name__ == '__main__':

    print("This function will check the list and returns a set of unique elements")
    list = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
    result = unique_elements(list)
    print(result)
