import matplotlib.pyplot as plt
import random

def insertion_sort(arr):
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            comparisons += 1
        arr[j + 1] = key
    return comparisons

# Generate a random list of integers for sorting
random.seed(42)
array_to_sort = [random.randint(1, 100) for _ in range(20)]

# Make a copy of the original list for sorting
sorted_array = array_to_sort.copy()

# Sort the list using Insertion Sort and record the number of comparisons
comparisons = insertion_sort(sorted_array)

# Print the sorted list and the number of comparisons made
print("Sorted array:", sorted_array)
print("Number of comparisons:", comparisons)

# Create a bar chart to visualize the number of comparisons
plt.bar(['Insertion Sort'], [comparisons])
plt.ylabel('Number of Comparisons')
plt.title('Comparison Count for Insertion Sort')
plt.show()
