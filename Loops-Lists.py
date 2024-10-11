"""
Loops and Lists
Write a function find_common_elements(list1, list2) that takes two lists as arguments and
returns a new list containing only the elements that are common between them. 
The function should not include duplicate elements in the output list.
Example:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(find_common_elements(list1, list2)) # Output: [4,
5]

"""

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

if __name__ == '__main__':

    print("This Function will take 2 arrays and check the common elements from the lists")
    list1 = list(map(int, input("Enter the first list of numbers separated by spaces: ").split()))
    list2 = list(map(int, input("Enter the second list of numbers separated by spaces: ").split()))

    result = find_common_elements(list1, list2)

    print(result)
