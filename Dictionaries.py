"""
Dictionaries and Functions Write a function char_count(string) that takes a string as input and returns a dictionary where
the keys are the characters in the string and the values are the counts of how many times each character appears.
Example:
string = hello world;
print(char_count(string))
# Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
"""

def char_count(string):
    count_dict = {}
    for char in string: # loop iterates through each character
        if char in count_dict: # if it is already in the dictionary
            count_dict[char] += 1 # count char + 1
        else:
            count_dict[char] = 1
    return count_dict

if __name__ == '__main__':

    print("This function will count the number of character in the string")
    string = input("Enter a string: ")
    result = char_count(string)
    print(result)
