def is_subset(arr1, arr2):
    # Create a hash map for arr2
    seen = {}

    # Store all elements of arr2
    for num in arr2:
        seen[num] = True

    # Check every element of arr1
    for num in arr1:
        if num not in seen:
            return False

    return 1


# Driver code
arr1 = [1, 3, 4, 5, 2]
arr2 = [2, 4, 3, 1, 7, 5, 15]

if is_subset(arr1, arr2):
    print("arr1[] is a subset of arr2[]")
else:
    print("arr1[] is not a subset of arr2[]")