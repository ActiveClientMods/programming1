import random
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


def merge_sort(unsorted_arr):
    
    if len(unsorted_arr) <= 1:
        return unsorted_arr

    mid = len(unsorted_arr) // 2
    left_half = unsorted_arr[:mid]
    right_half = unsorted_arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    sorted_arr = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_arr.append(left[left_index])
            left_index += 1
        else:
            sorted_arr.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        sorted_arr.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        sorted_arr.append(right[right_index])
        right_index += 1

    return sorted_arr

z = 1000000
unsorted_arr = random.sample(range(1,(z + 1)), z)

print("Unsorted Array")
print(unsorted_arr)
print()
print()
logging.info('Sort will begin')
sorted_arr = merge_sort(unsorted_arr)
logging.info('Sort finished')
print("Sorted Array")
print(sorted_arr)

 