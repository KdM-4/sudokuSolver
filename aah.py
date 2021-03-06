def findUnique(arr):
    uniques = []
    # Insert all array elements in hash table
    mp = {}
    for i in range(len(arr)):
        if arr[i] not in mp:
            mp[arr[i]] = 0
        mp[arr[i]] += 1

    # Traverse through map only and
    for x in mp:
        if mp[x] == 1:
            uniques.append(x)

    return uniques


arr = [9, 4, 9, 6, 7, 4]
print(findUnique(arr))