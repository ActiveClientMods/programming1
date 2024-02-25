import random
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def bubble_sort(unsorted_arr):
    logging.info('Sort will begin')
    n = len(unsorted_arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if unsorted_arr[j] > unsorted_arr[j+1]:
                unsorted_arr[j], unsorted_arr[j+1] = unsorted_arr[j+1], unsorted_arr[j]
    logging.info('Sort finished')
    return unsorted_arr
    

z = 100000
unsorted_arr = random.sample(range(1,(z + 1)), z)

print("Unsorted Array")
print(unsorted_arr)
print()
print()
sorted_arr = bubble_sort(unsorted_arr)
print("Sorted Array")
print(sorted_arr)
