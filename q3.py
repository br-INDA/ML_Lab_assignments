def common_ele(l1, l2):
    count = 0
    visited = []
    # Count common elements between l1 and l2 without counting duplicates
    for ele in l1:
        if ele in l2 and ele not in visited:
            count += 1
            visited.append(ele)
    return count

#main
list1 = [34, 42, 22, 12, 5]
list2 = [22, 34, 5, 16, 77]
result = common_ele(list1, list2)
print("Number of common elements:", result)
