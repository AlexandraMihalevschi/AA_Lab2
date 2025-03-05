import time
import sys
import random
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def generate_lists(size):
    ordered = list(range(size))
    reversed_list = list(range(size, 0, -1))
    random_list = random.sample(range(size), size)
    random_duplicates = [random.choice(range(size // 2)) for _ in range(size)]
    random_floats = [random.uniform(0, 100) for _ in range(size)]
    half_sorted = ordered[:size // 2] + random.sample(range(size // 2, size), size // 2)
    return ordered, reversed_list, random_list, random_duplicates, random_floats, half_sorted

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
        sorted_list = insertion_sort(temp_list)
        end_time = time.time()
        times.append(end_time - start_time)
        spaces.append(sys.getsizeof(sorted_list))

    return labels, times, spaces

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

    plt.title("Insertion Sort Performance Analysis")
    plt.show()

def analyze_performance_over_range(start, end, step):
    sizes = list(range(start, end + 1, step))
    times = []
    spaces = []

    for size in sizes:
        random_list = random.sample(range(size), size)  # Only using the random list
        _, time_taken, space_used = analyze_sorting(size)
        times.append(time_taken[2])  # Only using the time for the random list
        spaces.append(space_used[2])  # Only using the space for the random list

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

    plt.title("Insertion Sort Performance: Time & Space Complexity (Random Ordered List)")
    plt.show()

sizes_to_test = [500, 1000, 5000, 10000]

for size in sizes_to_test:
    print(f"Analyzing Insertion Sort performance for size: {size}")
    labels, times, spaces = analyze_sorting(size)
    plot_results(labels, times, spaces)

analyze_performance_over_range(500, 10000, 5000)
