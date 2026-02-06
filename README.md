
# Algorithm Analysis – Sorting Algorithms

## 📝 Project Description

This project is part of an Algorithm Analysis assignment.  
The goal is to implement and analyze different sorting algorithms in Python, focusing on their correctness and theoretical time complexity.

Each algorithm is implemented from scratch, documented with a clear description and Big-O complexity analysis, and validated using unit tests.

---

## 🛠️ Implemented Algorithms

The following sorting algorithms have been implemented:

1. **Bubble Sort**
2. **Insertion Sort**
3. **Selection Sort**
4. **Merge Sort**
5. **Quick Sort**

Each algorithm:
- Is implemented in a separate Python file
- Does not modify the original input list
- Includes comments describing how the algorithm works
- Includes time complexity analysis (best, average, and worst cases)

---

## ⏰ Time Complexity Summary

| Algorithm       | Best Case | Average Case | Worst Case |
|-----------------|-----------|--------------|------------|
| Bubble Sort     | O(n²)     | O(n²)        | O(n²)     |
| Insertion Sort  | O(n)      | O(n²)        | O(n²)     |
| Selection Sort  | O(n²)     | O(n²)        | O(n²)     |
| Merge Sort      | O(n log n)| O(n log n)   | O(n log n)|
| Quick Sort      | O(n log n)| O(n log n)   | O(n²)     |

---

## 📂 Project Structure

Algorithm-Analysis/
│
├── algorithms/
│   ├── __init__.py
│   ├── bubble_sort.py
│   ├── insertion_sort.py
│   ├── selection_sort.py
│   ├── merge_sort.py
│   └── quick_sort.py
│
├── experiments/
│   ├── benchmark.py
│   └── benchmark_results.csv
│
├── tests/
│   ├── test_bubble_sort.py
│   ├── test_insertion_sort.py
│   ├── test_selection_sort.py
│   ├── test_merge_sort.py
│   └── test_quick_sort.py
│
├── notebook/
│   └── experimental_analysis.ipynb
│
├── README.md
├──

---

## 👥 Authors

- [Jeisson Sanchez](https://github.com/JeissonS02)
- [Sebastian Albarracin](https://github.com/SebastianAlbarracinSilva)
