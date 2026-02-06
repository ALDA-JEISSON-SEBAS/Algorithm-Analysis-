import random
import time
import pandas as pd
import os


from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.selection_sort import selection_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort


# Input sizes to test
SIZES = [100, 500, 1000, 2000, 5000]

# Number of repetitions for averaging
REPETITIONS = 5


def measure_time(algorithm, data):
    """
    Measures execution time of a sorting algorithm.
    """
    start = time.perf_counter()
    algorithm(data)
    end = time.perf_counter()
    return end - start


def run_benchmark():
    results = []

    for size in SIZES:
        for _ in range(REPETITIONS):

            # Generate the same random data for all algorithms
            base_data = [random.randint(0, 10000) for _ in range(size)]

            algorithms = {
                "Bubble Sort": bubble_sort,
                "Insertion Sort": insertion_sort,
                "Selection Sort": selection_sort,
                "Merge Sort": merge_sort,
                "Quick Sort": quick_sort
            }

            for name, algorithm in algorithms.items():
                data_copy = base_data.copy()
                elapsed_time = measure_time(algorithm, data_copy)

                results.append({
                    "Algorithm": name,
                    "Input Size": size,
                    "Time (seconds)": elapsed_time
                })

    return pd.DataFrame(results)


if __name__ == "__main__":
    df = run_benchmark()
    output_path = os.path.join(os.path.dirname(__file__), "benchmark_results.csv")
    df.to_csv(output_path, index=False)
    print("Benchmark completed. Results saved to benchmark_results.csv")
