import time
import sys
import random
import matplotlib.pyplot as plt

# Import sorting functions from each of the sorting files
from Heap_Sort import heap_sort
from Quick_Sort import quick_sort
from Merge_Sort import merge_sort
from Insertion_Sort import insertion_sort


# Function to create a random list of size `size`
def generate_random_list(size):
    return [random.randint(0, size) for _ in range(size)]


# Function to analyze sorting for a random list of size `size`
def analyze_sorting_algorithms(size):
    # Generate a random list
    random_list = generate_random_list(size)

    # Timing and Space for Heap Sort
    temp_list = random_list[:]
    start_time = time.time()
    heap_sort(temp_list)
    end_time = time.time()
    time_heap = end_time - start_time
    space_heap = sys.getsizeof(temp_list)

    # Timing and Space for Quick Sort
    temp_list = random_list[:]
    start_time = time.time()
    quick_sort(temp_list)
    end_time = time.time()
    time_quick = end_time - start_time
    space_quick = sys.getsizeof(temp_list)

    # Timing and Space for Merge Sort
    temp_list = random_list[:]
    start_time = time.time()
    merge_sort(temp_list)
    end_time = time.time()
    time_merge = end_time - start_time
    space_merge = sys.getsizeof(temp_list)

    # Timing and Space for Insertion Sort
    temp_list = random_list[:]
    start_time = time.time()
    insertion_sort(temp_list)
    end_time = time.time()
    time_insertion = end_time - start_time
    space_insertion = sys.getsizeof(temp_list)

    return time_heap, time_quick, time_merge, time_insertion, space_heap, space_quick, space_merge, space_insertion


# Function to plot results for sorting algorithms (time and space complexity)
def plot_results(time_heap, time_quick, time_merge, time_insertion, space_heap, space_quick, space_merge,
                 space_insertion):
    labels = ['Heap Sort', 'Quick Sort', 'Merge Sort', 'Insertion Sort']

    # Plotting Time Complexity
    fig, ax1 = plt.subplots(figsize=(10, 6))

    ax1.set_xlabel('Sorting Algorithms')
    ax1.set_ylabel('Time (s)', color='tab:blue')
    ax1.bar(labels, [time_heap, time_quick, time_merge, time_insertion], color='tab:blue', alpha=0.6, label='Time')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    # Plotting Space Complexity
    ax2 = ax1.twinx()
    ax2.set_ylabel('Space (bytes)', color='tab:red')
    ax2.plot(labels, [space_heap, space_quick, space_merge, space_insertion], color='tab:red', marker='o',
             linestyle='dashed', label='Space')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    # Adjust layout and show the plot
    plt.title('Comparison of Sorting Algorithms (Time and Space Complexity)')
    plt.show()


# Analyze the sorting algorithms for a random list of 10,000 elements
time_heap, time_quick, time_merge, time_insertion, space_heap, space_quick, space_merge, space_insertion = analyze_sorting_algorithms(
    10000)

# Plot the results
plot_results(time_heap, time_quick, time_merge, time_insertion, space_heap, space_quick, space_merge, space_insertion)
