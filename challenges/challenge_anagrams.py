def merge(arr, L, R):
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
    return arr


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        arr = merge(arr, L, R)


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    first = list(first_string)
    second = list(second_string)
    mergeSort(first)
    mergeSort(second)
    return first == second

# https://www.geeksforgeeks.org/merge-sort/
