
# Matrix Multiplication using MapReduce

A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

# MAP phase
mapped = []

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            key = (i, j)
            value = A[i][k] * B[k][j]
            mapped.append((key, value))

# SHUFFLE phase
grouped = {}

for key, value in mapped:
    if key not in grouped:
        grouped[key] = []
    grouped[key].append(value)

# REDUCE phase
C = []

for i in range(len(A)):
    row = []
    for j in range(len(B[0])):
        row.append(sum(grouped[(i, j)]))
    C.append(row)

# Display result
print("Resultant Matrix:")
for row in C:
    print(row)
