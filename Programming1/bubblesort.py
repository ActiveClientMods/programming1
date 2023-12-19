import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Generate an array with 1000 random unique entries
arr = random.sample(range(1, 1001), 1000)

for i in range(100):
    bubble_sort(arr)
    print(arr)
