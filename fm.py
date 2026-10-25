
# Flajolet-Martin Algorithm

stream = [1, 2, 3, 4, 5, 2, 1]

# Hash function
def hash_value(x):
    return (x * 2654435761) & 0xFFFFFFFF

# Count trailing zeros in binary
def trailing_zeros(n):
    if n == 0:
        return 32

    count = 0
    while n % 2 == 0:
        count += 1
        n = n // 2
    return count

# Find maximum trailing zeros
max_zeros = 0

for x in stream:
    h = hash_value(x)
    binary = format(h, '032b')
    zeros = trailing_zeros(h)

    print(x, "->", binary, "->", zeros, "zeros")

    if zeros > max_zeros:
        max_zeros = zeros

# Estimate distinct elements
estimate = 2 ** max_zeros

print("Maximum trailing zeros:", max_zeros)
print("Estimated distinct elements:", estimate)
