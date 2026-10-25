
# DGIM Algorithm

stream = [1, 0, 1, 1, 0, 1, 0, 1]
N = 5
buckets = []
time = 0

for bit in stream:
    time += 1

    # Step 1: Create a bucket for every 1
    if bit == 1:
        buckets.insert(0, [1, time])

        # Step 2: Merge buckets if more than 2 have same size
        size = 1
        while True:
            indexes = [i for i, b in enumerate(buckets)
                       if b[0] == size]

            if len(indexes) <= 2:
                break

            # Merge the two oldest buckets
            i, j = indexes[-2], indexes[-1]
            merged = [size * 2, buckets[i][1]]

            del buckets[j]
            del buckets[i]
            buckets.insert(i, merged)

            size *= 2

    # Step 3: Remove expired buckets
    buckets = [b for b in buckets if b[1] > time - N]

# Step 4: Estimate number of 1s
if buckets:
    estimate = sum(b[0] for b in buckets) - buckets[-1][0] // 2
else:
    estimate = 0

print("Buckets:", buckets)
print("Estimated number of 1s:", estimate)
