"""
Advanced Functions and Sets
Write a function find_pairs_with_sum(nums,
target_sum) that finds all pairs of numbers in a list
nums that add up to target_sum. The function should
return a set of tuples, where each tuple
contains a unique pair of numbers.
Example:
nums = [2, 4, 3, 5, 7, 8, 9]
target_sum = 10
print(find_pairs_with_sum(nums, target_sum))
# Output: {(3, 7), (2, 8), (4, 6)}
"""

def find_pairs_with_sum(nums, target_sum):
    seen = set()
    pairs = set()
    for num in nums:
        complement = target_sum - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    return pairs

if __name__ == '__main__':

    print("This function will take the n no. of number and return the pair of number whose sum is equal to the targeted number")
    nums = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
    target_sum = int(input("Enter the target sum: "))
    print(f"The pair of number whose sum is {target_sum}")
    print(find_pairs_with_sum(nums, target_sum))
