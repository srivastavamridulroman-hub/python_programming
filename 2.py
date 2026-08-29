# Find the largest element in an array

a = [3, 7, 2, 9, 5, 1]

largest = a[0]

for i in range(1, len(a)):
    if a[i] > largest:
        largest = a[i]

print(largest)