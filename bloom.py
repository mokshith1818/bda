
# Bloom Filter using two polynomial hash functions

size = 10
bit_array = [0] * size

# First polynomial hash function
def hash1(x):
    return (2*x*x + 3*x + 1) % size

# Second polynomial hash function
def hash2(x):
    return (x*x*x + 2*x + 4) % size

# Insert number into Bloom Filter
def add(x):
    bit_array[hash1(x)] = 1
    bit_array[hash2(x)] = 1

# Check whether number may be present
def check(x):
    if bit_array[hash1(x)] == 1 and bit_array[hash2(x)] == 1:
        print(x, "may be present")
    else:
        print(x, "is definitely not present")

# Insert elements
numbers = [10, 20, 30]

for x in numbers:
    add(x)

print("Bit array:", bit_array)

# Search elements
check(20)
check(40)
