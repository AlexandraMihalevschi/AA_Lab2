import time
import sys
import random
import matplotlib.pyplot as plt

def heapify(arr, n, i):
    largest = i
    l = 2*i+1
    r = 2*i+2

    if l<n and arr[l]>arr[largest]:
        largest = l
    if r<n and arr[r]>arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

    return arr

def generate_lists(size):
    ordered = list(range(size))
    reversed_list = list(range(size, 0, -1))
    random_list = random.sample(range(size), size)
    random_duplicates = [random.choice(range(size // 2)) for _ in range(size)]
    random_floats = [random.uniform(0, 100) for _ in range(size)]
    half_sorted = ordered[:size // 2] + random.sample(range(size // 2, size), size // 2)
    return ordered, reversed_list, random_list, random_duplicates, random_floats, half_sorted

# Function to analyze sorting performance
def analyze_sorting(size):
    lists = generate_lists(size)
    labels = [
        "Ordered", "Reversed", "Random",
        "Duplicates", "Floats", "Half"
    ]
    times = []
    spaces = []

    for lst in lists:
        temp_list = lst[:]
        start_time = time.time()
        sorted_list = heap_sort(temp_list)
        end_time = time.time()
        times.append(end_time - start_time)
        spaces.append(sys.getsizeof(sorted_list))

    return labels, times, spaces

# Function to plot the results
def plot_results(labels, times, spaces):
    fig, ax1 = plt.subplots()
    ax1.set_xlabel("List Type")
    ax1.set_ylabel("Time (s)", color='tab:blue')
    ax1.bar(labels, times, color='tab:blue', alpha=0.6, label='Time')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    ax2 = ax1.twinx()
    ax2.set_ylabel("Space (bytes)", color='tab:red')
    ax2.plot(labels, spaces, color='tab:red', marker='o', linestyle='dashed', label='Space')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    plt.title("Heap Sort Performance Analysis")
    plt.show()

# Function to analyze performance over a range of sizes
def analyze_performance_over_range(start, end, step):
    sizes = list(range(start, end + 1, step))
    times = []
    spaces = []

    for size in sizes:
        _, time_taken, space_used = analyze_sorting(size)
        times.append(sum(time_taken) / len(time_taken))
        spaces.append(sum(space_used) / len(space_used))

    fig, ax1 = plt.subplots()
    ax1.set_xlabel("Number of Elements")
    ax1.set_ylabel("Average Time (s)", color='tab:blue')
    ax1.plot(sizes, times, marker='o', linestyle='-', color='b', label='Time Complexity')
    ax1.tick_params(axis='y', labelcolor='tab:blue')
    ax1.grid()

    ax2 = ax1.twinx()
    ax2.set_ylabel("Average Space (bytes)", color='tab:red')
    ax2.plot(sizes, spaces, marker='s', linestyle='--', color='r', label='Space Complexity')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    plt.title("Heap Sort Performance: Time & Space Complexity")
    plt.show()

    sizes = list(range(start, end + 1, step))
    times = []

    for size in sizes:
        _, time_taken, _ = analyze_sorting(size)
        times.append(sum(time_taken) / len(time_taken))

    plt.figure(figsize=(12, 7))
    plt.plot(sizes, times, marker='o', linestyle='-', color='b')
    plt.xlabel("Number of Elements")
    plt.ylabel("Average Time (s)")
    plt.title("Heap Sort Performance Over Different Input Sizes")
    plt.grid()
    plt.show()

# Sizes to test
sizes_to_test = [500, 1000, 5000, 10000, 50000, 100000]

for size in sizes_to_test:
    print(f"Analyzing Heap Sort performance for size: {size}")
    labels, times, spaces = analyze_sorting(size)
    plot_results(labels, times, spaces)

# Analyze performance for a range of sizes
analyze_performance_over_range(500, 100000, 5000)
