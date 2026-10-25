
def hash1(x):
    return (5*x + 3) % 16

def trailing_zero(n):
    if n == 0:
        return 4

    count = 0
    while n % 2 == 0:
        count += 1
        n = n // 2
    return count

data = [1, 2, 3, 5, 4, 5, 1, 2, 3]

hash_values = []
binary = []
zero = []

for i in data:
    hash_values.append(hash1(i))

for i in hash_values:
    binary.append(bin(i)[2:])

for i in hash_values:
    zero.append(trailing_zero(i))

print("Hash values:", hash_values)
print("Binary values:", binary)
print("Trailing zeros:", zero)
print("Estimated Unique Elements:", 2 ** max(zero))
