
import random


matrix = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]


print("Matrix:")
for row in matrix:
    print(row)


row_sums = [sum(row) for row in matrix]


col_sums = [sum(row[i] for row in matrix) for i in range(3)]


diag1_sum = sum(matrix[i][i] for i in range(3))
diag2_sum = sum(matrix[i][2-i] for i in range(3))

# s
print("\nRow sums:", row_sums)
print("Column sums:", col_sums)
print("Main diagonal sum:", diag1_sum)
print("Secondary diagonal sum:", diag2_sum)




