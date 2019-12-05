# 2 almost identical arrays are given to you with 1 missing element in array


def find_missing_element(arr1, arr2):
    arr1.sort()
    arr2.sort()
    if len(arr1) > len(arr2):
        return arr2[len(arr2) - 1]
    elif len(arr2) > len(arr1):
        return arr2[len(arr2) - 1]
    return "Both Arrays have Same no of elements"

