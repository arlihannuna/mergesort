def merge(left, right):
    return_array = []
    flag = True
    while flag:
        if len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                return_array.append(left[0])
                left.pop(0)
                continue
            else:
                return_array.append(right[0])
                right.pop(0)
                continue
        if len(left) > 0:
            return_array.append(left[0])
            left.pop(0)
            continue
        elif len(right) > 0:
            return_array.append(right[0])
            right.pop(0)
            continue
        else:
            flag = False

    return return_array


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:

        # Create right ← A[start..mid] and right ← A[mid+1..end]
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Sort the two halves
        left = mergeSort(left)
        right = mergeSort(right)

        return merge(left, right)


arr_ = [10, 9, 2, 4, 6, 13]
sorted_arr = mergeSort(arr_)
print(sorted_arr)

