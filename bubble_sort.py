def bubble_sort(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    print(arr)


arr_ = [8, 5, 6, 3, 1, 2, 4]
bubble_sort(arr_)
