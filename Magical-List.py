
numbers = [12, 45, 78, 23, 56, 89, 67, 33, 22]

numbers.sort(reverse=False)
print("Sorted List (Ascending):", numbers)

numbers.sort(reverse=True)
print("Sorted List (Descending):", numbers)

magical_tuple = tuple(numbers)
print("Tuple of Magical Numbers:", magical_tuple)

most_magical = max(magical_tuple)
least_magical = min(magical_tuple)

print("Most Magical Number:", most_magical)
print("Least Magical Number:", least_magical)
