# NumPy Analyzer Toolkit (OOP-Based) 🚀

A Python-based data analytics application that integrates **NumPy** functionalities with **Object-Oriented Programming (OOP)** principles. This toolkit provides a robust, menu-driven interface to perform array management, element-wise math, matrix operations, advanced searching/sorting/filtering, and comprehensive statistical analysis.

---

## 📋 Features & Requirements

This project fulfills all core specifications of the project blueprint:

### 1. Object-Oriented Programming (OOP) Structure
* **Class Encapsulation**: Built around a core `DataAnalytics` class to encapsulate all data and operations.
* **Encapsulation & Private Methods**: Implements private helper methods (e.g., `_is_empty()`) for internal state checking.
* **Class & Static Methods**: 
  * `@classmethod` (`create_random`): Generates arrays with randomized values based on shape and bounds.
  * `@staticmethod` (`show_welcome`): Displays utility headers and banner messages.

### 2. Array Management
* **Creation, Indexing, and Slicing**: Supports 1D, 2D, and 3D arrays with custom indexing and slicing capabilities.
* **Combining and Splitting**: Concatenate multiple arrays along specific axes or split arrays into smaller sections using `np.concatenate` and `np.array_split`.

### 3. Mathematical & Matrix Operations
* **Element-Wise Operations**: Perform addition, subtraction, multiplication, and division across arrays or scalars.
* **Matrix Algebra**: Compute dot products (`np.dot`) and matrix multiplication (`np.matmul`) for 2D arrays.

### 4. Search, Sort, and Filter
* **Search**: Locate specific values within arrays using `np.where()`.
* **Sort**: Sort elements in ascending or descending order.
* **Filter**: Extract and filter elements based on user-defined condition rules.

### 5. Aggregating Functions & Statistics
* **Summary Statistics**: Compute sum, mean, median, standard deviation, and variance.
* **Percentiles**: Calculate statistical percentiles (e.g., 25th, 50th, 75th).
* **Correlation**: Compute correlation coefficient matrices between arrays.

### 6. Interactive User Interface (UI)
* An intuitive, menu-driven console loop that allows users to easily navigate through options and exit gracefully.

---

## ⚙️ Prerequisites

Ensure you have the following installed on your system:
* **Python 3.x**
* **NumPy Library**

---

## 📥 Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/your-username/numpy-analyzer-toolkit.git](https://github.com/your-username/numpy-analyzer-toolkit.git)
   cd numpy-analyzer-toolkit
   pip install numpy
   python numpy_analyzer.py
   ========================================
      NUMPY ANALYZER TOOLKIT (OOP)
========================================

--- MENU ---
1. Enter Custom Array
2. Create Random Array
3. View Array Info
4. Combine Array
5. Split Array
6. Basic Math Operations (+, -, *, /)
7. Matrix Multiplication / Dot Product
8. Search Value
9. Sort Array
10. Filter Values (Greater than X)
11. Show Aggregates / Statistics
12. Show Correlation Coefficient
13. Exit

Select option (1-13):

numpy-analyzer/
│

├── numpy_analyzer.py    # Main script containing DataAnalytics class & CLI menu

└── README.md            # Project documentation
