import numpy as np


class DataAnalytics:

    def __init__(self, data=None):
        # Array initialize karne ke liye constructor
        if data is not None:
            self.data = np.array(data)
        else:
            self.data = np.array([])

    # Private method array empty hai ya nahi check karne ke liye
    def _is_empty(self):
        return self.data.size == 0

    # Class method random array create karne ke liye
    @classmethod
    def create_random(cls, shape, low=1, high=100):
        random_arr = np.random.randint(low, high, size=shape)
        return cls(random_arr)

    # Static method utility banner ke liye
    @staticmethod
    def show_welcome():
        print("\n" + "=" * 40)
        print("      NUMPY ANALYZER TOOLKIT (OOP)")
        print("=" * 40)

    # --- Array Management ---
    def set_array(self, new_data):
        self.data = np.array(new_data)
        print("\nArray successfully set:")
        print(self.data)

    def print_info(self):
        if self._is_empty():
            print("\nArray is empty!")
            return
        print(f"\nCurrent Array:\n{self.data}")
        print(f"Shape: {self.data.shape}")
        print(f"Dimensions: {self.data.ndim}")
        print(f"Data Type: {self.data.dtype}")

    def combine_with(self, other_list, axis=0):
        if self._is_empty():
            print("Current array is empty!")
            return
        try:
            other_arr = np.array(other_list)
            combined = np.concatenate((self.data, other_arr), axis=axis)
            print("\nCombined Array:")
            print(combined)
        except Exception as e:
            print("Error combining arrays:", e)

    def split_into(self, parts, axis=0):
        if self._is_empty():
            print("Current array is empty!")
            return
        try:
            result = np.array_split(self.data, parts, axis=axis)
            print("\nSplit Arrays:")
            for i, part in enumerate(result, 1):
                print(f"Part {i}:\n{part}")
        except Exception as e:
            print("Error splitting array:", e)

    # --- Mathematical Operations ---
    def basic_operation(self, other_val, op_type):
        if self._is_empty():
            print("Current array is empty!")
            return
        other_arr = np.array(other_val)

        if op_type == "add":
            res = self.data + other_arr
        elif op_type == "sub":
            res = self.data - other_arr
        elif op_type == "mul":
            res = self.data * other_arr
        elif op_type == "div":
            res = self.data / other_arr
        else:
            print("Invalid operation!")
            return

        print(f"\nResult of {op_type}:")
        print(res)

    def matrix_mul(self, other_matrix):
        if self._is_empty():
            print("Current array is empty!")
            return
        try:
            other_arr = np.array(other_matrix)
            # Dot product and matrix multiplication
            dot_res = np.dot(self.data, other_arr)
            matmul_res = np.matmul(self.data, other_arr)

            print("\nDot Product:\n", dot_res)
            print("\nMatrix Multiplication:\n", matmul_res)
        except Exception as e:
            print("Matrix operation error:", e)

    # --- Search, Sort, and Filter ---
    def search_val(self, val):
        if self._is_empty():
            print("Current array is empty!")
            return
        indices = np.where(self.data == val)
        if len(indices[0]) > 0:
            print(f"Value {val} found at indices:", indices)
        else:
            print(f"Value {val} not found in array.")

    def sort_arr(self, order="asc"):
        if self._is_empty():
            print("Current array is empty!")
            return
        sorted_arr = np.sort(self.data)
        if order.lower() == "desc":
            sorted_arr = np.flip(sorted_arr)
        print(f"\nSorted Array ({order}):")
        print(sorted_arr)

    def filter_greater_than(self, val):
        if self._is_empty():
            print("Current array is empty!")
            return
        # Condition filtering
        filtered = self.data[self.data > val]
        print(f"\nElements greater than {val}:")
        print(filtered)

    # --- Aggregating Functions ---
    def calculate_stats(self):
        if self._is_empty():
            print("Current array is empty!")
            return

        print("\n--- Statistical Analysis ---")
        print("Sum:", np.sum(self.data))
        print("Mean:", np.mean(self.data))
        print("Median:", np.median(self.data))
        print("Std Dev:", np.std(self.data))
        print("Variance:", np.var(self.data))
        print("25th Percentile:", np.percentile(self.data, 25))
        print("75th Percentile:", np.percentile(self.data, 75))

    def calculate_correlation(self, other_list):
        if self._is_empty():
            print("Current array is empty!")
            return
        try:
            other_arr = np.array(other_list)
            corr = np.corrcoef(self.data.flatten(), other_arr.flatten())
            print("\nCorrelation Matrix:")
            print(corr)
        except Exception as e:
            print("Error calculating correlation:", e)


# --- Menu Interface (UI) ---
def main():
    DataAnalytics.show_welcome()
    analyzer = DataAnalytics()

    while True:
        print("\n--- MENU ---")
        print("1. Enter Custom Array")
        print("2. Create Random Array")
        print("3. View Array Info")
        print("4. Combine Array")
        print("5. Split Array")
        print("6. Basic Math Operations (+, -, *, /)")
        print("7. Matrix Multiplication / Dot Product")
        print("8. Search Value")
        print("9. Sort Array")
        print("10. Filter Values (Greater than X)")
        print("11. Show Aggregates / Statistics")
        print("12. Show Correlation Coefficient")
        print("13. Exit")

        choice = input("\nSelect option (1-13): ").strip()

        if choice == "1":
            raw_input = input(
                "Enter elements as python list (e.g. [1, 2, 3] or [[1, 2], [3, 4]]): "
            )
            try:
                data = eval(raw_input)
                analyzer.set_array(data)
            except:
                print("Invalid format!")

        elif choice == "2":
            shape_str = input(
                "Enter shape tuple (e.g., (3, 3) or (5,)): "
            )
            try:
                shape = eval(shape_str)
                analyzer = DataAnalytics.create_random(shape)
                print("\nRandom Array Created:")
                print(analyzer.data)
            except:
                print("Invalid shape!")

        elif choice == "3":
            analyzer.print_info()

        elif choice == "4":
            other = input("Enter second array/list to concatenate: ")
            try:
                analyzer.combine_with(eval(other))
            except:
                print("Invalid input!")

        elif choice == "5":
            parts = input("Enter number of parts to split: ")
            if parts.isdigit():
                analyzer.split_into(int(parts))
            else:
                print("Enter a valid number.")

        elif choice == "6":
            op = input("Enter operation (add/sub/mul/div): ").strip().lower()
            val = input("Enter scalar or list: ")
            try:
                analyzer.basic_operation(eval(val), op)
            except:
                print("Invalid input!")

        elif choice == "7":
            other = input("Enter second 2D list/matrix: ")
            try:
                analyzer.matrix_mul(eval(other))
            except:
                print("Invalid matrix input!")

        elif choice == "8":
            val = input("Enter value to search: ")
            try:
                analyzer.search_val(eval(val))
            except:
                print("Invalid value!")

        elif choice == "9":
            order = input("Sort order - asc or desc: ").strip()
            analyzer.sort_arr(order)

        elif choice == "10":
            val = input("Show numbers greater than: ")
            try:
                analyzer.filter_greater_than(float(val))
            except:
                print("Invalid number!")

        elif choice == "11":
            analyzer.calculate_stats()

        elif choice == "12":
            other = input("Enter second array/list for correlation: ")
            try:
                analyzer.calculate_correlation(eval(other))
            except:
                print("Invalid input!")

        elif choice == "13":
            print("\nThank you for using NumPy Analyzer!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()