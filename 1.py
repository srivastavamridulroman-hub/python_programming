# Count the frequency of each element

arr = [1, 4, 5, 9, 7, 7, 1, 4, 4, 7, 7]

freq_map = dict()

for i in range(0, len(arr)):
    if arr[i] in freq_map:
        freq_map[arr[i]] += 1
    else:
        freq_map[arr[i]] = 1

print(freq_map)