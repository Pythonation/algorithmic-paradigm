array = [3 ,5 , 8,13 ,21 ,34 ,55 ,77 ,144 ,233 ,377 ]
x = 77

def binary_search(arr, key):
    start = 0
    end = len(arr)
    while start < end:
        mid = (start + end)//2
        if arr[mid] > key:
            end = mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            return mid
    return -1

print(binary_search(array,x))


