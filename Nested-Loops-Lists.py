"""
Nested Loops and Lists
Write a function flatten_matrix(matrix) that takes a 2D
list (matrix) as input and returns a
flattened 1D list containing all the elements of the
matrix.
Example:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(flatten_matrix(matrix)) # Output: [1, 2, 3, 4, 5, 6, 7,
8, 9]
"""

def flatten_matrix(matrix):
    flattened = [] # to store the elements.
    for row in matrix: # loop iterates over each row in the matrix.
        for element in row: # loop iterates over each element in the row
            flattened.append(element) # appends it to the flattened list.
    return flattened

if __name__ == '__main__':
    
    matrix = []
    print("To Enter your matrix")
    rows = int(input("First Enter the number of rows in the matrix: "))
    row_count = 0
    for _ in range(rows):
        row_count += 1
        row = list(map(int, input(f"Row number: {row_count} Enter the elements of the row separated by spaces: ").split()))
        matrix.append(row)
    
    print(flatten_matrix(matrix))
