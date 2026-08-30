# removing duplicates from unsorted array
arr = [4, 2, 4, 7, 2]

seen = {}
result = []

for val in arr:
    if val not in seen:
        result.append(val)
        seen[val] = 1


print(result)