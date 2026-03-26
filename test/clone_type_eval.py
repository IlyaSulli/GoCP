"""
Qualitative evaluation of each detection method across clone types.

Clone taxonomy:
  Type-1  -- Exact copy (whitespace / comment differences only)
  Type-2  -- Renamed identifiers (variables, parameters, function name)
  Type-3  -- Gapped clone (statements added, removed, or reordered)
  Type-4  -- Semantic clone (same logic, structurally different implementation)
  False   -- Not a clone (should be rejected by all methods)
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

from predictor import predict, available_methods

TEST_CASES = [

    # =========================================================================
    # TYPE-1: Exact / whitespace / comment differences only
    # =========================================================================

    ("Type-1", "Identical (Kadane)", 1,
     """\
def max_subarray(arr):
    best = cur = arr[0]
    for x in arr[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
""",
     """\
def max_subarray(arr):
    best = cur = arr[0]
    for x in arr[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
"""),

    ("Type-1", "Docstring added", 1,
     """\
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
""",
     """\
def factorial(n):
    \"\"\"Return n factorial.\"\"\"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
"""),

    ("Type-1", "Inline comments added", 1,
     """\
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
""",
     """\
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1  # init bounds
    while lo <= hi:
        mid = (lo + hi) // 2  # midpoint
        if arr[mid] == target:
            return mid  # found
        elif arr[mid] < target:
            lo = mid + 1  # go right
        else:
            hi = mid - 1  # go left
    return -1  # not found
"""),

    ("Type-1", "Extra blank lines", 1,
     """\
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
""",
     """\
def is_prime(n):

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
"""),

    ("Type-1", "Block comment before function", 1,
     """\
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
""",
     """\
# Euclidean algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
"""),

    ("Type-1", "Identical (bubble sort)", 1,
     """\
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
""",
     """\
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
"""),

    ("Type-1", "Docstring + inline comments", 1,
     """\
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []
""",
     """\
def two_sum(nums, target):
    \"\"\"Return indices of two numbers that sum to target.\"\"\"
    seen = {}  # value -> index
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]  # found pair
        seen[x] = i
    return []
"""),

    ("Type-1", "Identical (linear search)", 1,
     """\
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
""",
     """\
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
"""),

    ("Type-1", "Mixed blank lines and comments", 1,
     """\
def count_pairs(arr, target):
    seen = {}
    count = 0
    for x in arr:
        if target - x in seen:
            count += seen[target - x]
        seen[x] = seen.get(x, 0) + 1
    return count
""",
     """\
# Count pairs summing to target
def count_pairs(arr, target):
    seen = {}
    count = 0

    for x in arr:
        if target - x in seen:
            count += seen[target - x]
        seen[x] = seen.get(x, 0) + 1

    return count
"""),

    ("Type-1", "Identical (fibonacci)", 1,
     """\
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
""",
     """\
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
"""),

    # =========================================================================
    # TYPE-2: Renamed identifiers
    # =========================================================================

    ("Type-2", "Renamed vars (Kadane)", 1,
     """\
def max_subarray(arr):
    best = cur = arr[0]
    for x in arr[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
""",
     """\
def kadane(nums):
    max_sum = curr = nums[0]
    for n in nums[1:]:
        curr = max(n, curr + n)
        max_sum = max(max_sum, curr)
    return max_sum
"""),

    ("Type-2", "Renamed vars + function (binary search)", 1,
     """\
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
""",
     """\
def find_index(numbers, value):
    left, right = 0, len(numbers) - 1
    while left <= right:
        pivot = (left + right) // 2
        if numbers[pivot] == value:
            return pivot
        elif numbers[pivot] < value:
            left = pivot + 1
        else:
            right = pivot - 1
    return -1
"""),

    ("Type-2", "Renamed vars (bubble sort)", 1,
     """\
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
""",
     """\
def sort_list(data):
    size = len(data)
    for pass_num in range(size):
        for idx in range(0, size - pass_num - 1):
            if data[idx] > data[idx + 1]:
                data[idx], data[idx + 1] = data[idx + 1], data[idx]
    return data
"""),

    ("Type-2", "Renamed vars (GCD)", 1,
     """\
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
""",
     """\
def greatest_common_divisor(x, y):
    while y:
        x, y = y, x % y
    return x
"""),

    ("Type-2", "Renamed vars (two sum)", 1,
     """\
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []
""",
     """\
def find_pair(numbers, goal):
    visited = {}
    for pos, val in enumerate(numbers):
        if goal - val in visited:
            return [visited[goal - val], pos]
        visited[val] = pos
    return []
"""),

    ("Type-2", "Renamed vars (factorial)", 1,
     """\
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
""",
     """\
def compute_factorial(num):
    product = 1
    for k in range(2, num + 1):
        product *= k
    return product
"""),

    ("Type-2", "Renamed vars (linear search)", 1,
     """\
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
""",
     """\
def sequential_search(lst, value):
    for pos in range(len(lst)):
        if lst[pos] == value:
            return pos
    return -1
"""),

    ("Type-2", "Renamed vars (count pairs)", 1,
     """\
def count_pairs(arr, target):
    seen = {}
    count = 0
    for x in arr:
        if target - x in seen:
            count += seen[target - x]
        seen[x] = seen.get(x, 0) + 1
    return count
""",
     """\
def pair_count(numbers, goal):
    freq = {}
    total = 0
    for val in numbers:
        if goal - val in freq:
            total += freq[goal - val]
        freq[val] = freq.get(val, 0) + 1
    return total
"""),

    ("Type-2", "Renamed vars (is_prime)", 1,
     """\
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
""",
     """\
def check_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True
"""),

    ("Type-2", "Renamed vars (fibonacci)", 1,
     """\
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
""",
     """\
def fib_sequence(steps):
    prev, curr = 0, 1
    for _ in range(steps):
        prev, curr = curr, prev + curr
    return prev
"""),

    # =========================================================================
    # TYPE-3: Gapped clones (added/removed/reordered statements)
    # =========================================================================

    ("Type-3", "Guard statement added", 1,
     """\
def count_pairs(arr, target):
    seen = {}
    count = 0
    for x in arr:
        if target - x in seen:
            count += seen[target - x]
        seen[x] = seen.get(x, 0) + 1
    return count
""",
     """\
def count_pairs(arr, target):
    if not arr:
        return 0
    seen = {}
    count = 0
    for x in arr:
        if target - x in seen:
            count += seen[target - x]
        seen[x] = seen.get(x, 0) + 1
    return count
"""),

    ("Type-3", "Extra early return added", 1,
     """\
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []
""",
     """\
def two_sum(nums, target):
    if len(nums) < 2:
        return []
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []
"""),

    ("Type-3", "Swap assignment reordered", 1,
     """\
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
""",
     """\
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr
"""),

    ("Type-3", "Extra variable for readability", 1,
     """\
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
""",
     """\
def is_prime(n):
    if n < 2:
        return False
    limit = int(n ** 0.5) + 1
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True
"""),

    ("Type-3", "Extra accumulator initialised earlier", 1,
     """\
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
""",
     """\
def factorial(n):
    result = 1
    start = 2
    for i in range(start, n + 1):
        result *= i
    return result
"""),

    ("Type-3", "Bounds differ by 1 (equivalent)", 1,
     """\
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
""",
     """\
def binary_search(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return -1
"""),

    ("Type-3", "Default argument added", 1,
     """\
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
""",
     """\
def linear_search(arr, target, start=0):
    for i in range(start, len(arr)):
        if arr[i] == target:
            return i
    return -1
"""),

    ("Type-3", "Else clause on loop added", 1,
     """\
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
""",
     """\
def gcd(a, b):
    while b:
        a, b = b, a % b
    else:
        pass
    return a
"""),

    ("Type-3", "Explicit abs() added for robustness", 1,
     """\
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
""",
     """\
def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
"""),

    ("Type-3", "Max subarray with result variable", 1,
     """\
def max_subarray(arr):
    best = cur = arr[0]
    for x in arr[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
""",
     """\
def max_subarray(arr):
    cur = arr[0]
    best = arr[0]
    for x in arr[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    result = best
    return result
"""),

    # =========================================================================
    # TYPE-4: Semantic clones (same logic, different structure)
    # =========================================================================

    ("Type-4", "For vs while (primality)", 1,
     """\
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
""",
     """\
def check_prime(num):
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True
"""),

    ("Type-4", "Recursive vs iterative (fibonacci)", 1,
     """\
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
""",
     """\
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
"""),

    ("Type-4", "Recursive vs iterative (factorial)", 1,
     """\
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
""",
     """\
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
"""),

    ("Type-4", "Recursive vs iterative (GCD)", 1,
     """\
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
""",
     """\
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
"""),

    ("Type-4", "List comprehension vs for loop (filter)", 1,
     """\
def get_evens(nums):
    return [x for x in nums if x % 2 == 0]
""",
     """\
def get_evens(nums):
    result = []
    for x in nums:
        if x % 2 == 0:
            result.append(x)
    return result
"""),

    ("Type-4", "Sum via loop vs accumulate", 1,
     """\
def array_sum(arr):
    total = 0
    for x in arr:
        total += x
    return total
""",
     """\
def array_sum(arr):
    from functools import reduce
    return reduce(lambda a, b: a + b, arr, 0)
"""),

    ("Type-4", "Linear search vs index lookup", 1,
     """\
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
""",
     """\
def linear_search(arr, target):
    i = 0
    while i < len(arr):
        if arr[i] == target:
            return i
        i += 1
    return -1
"""),

    ("Type-4", "Max element: loop vs built-in style", 1,
     """\
def find_max(arr):
    m = arr[0]
    for x in arr[1:]:
        if x > m:
            m = x
    return m
""",
     """\
def find_max(arr):
    m = arr[0]
    i = 1
    while i < len(arr):
        if arr[i] > m:
            m = arr[i]
        i += 1
    return m
"""),

    ("Type-4", "Palindrome: slice vs loop", 1,
     """\
def is_palindrome(s):
    return s == s[::-1]
""",
     """\
def is_palindrome(s):
    lo, hi = 0, len(s) - 1
    while lo < hi:
        if s[lo] != s[hi]:
            return False
        lo += 1
        hi -= 1
    return True
"""),

    ("Type-4", "Count zeros: sum vs loop", 1,
     """\
def count_zeros(arr):
    return sum(1 for x in arr if x == 0)
""",
     """\
def count_zeros(arr):
    count = 0
    for x in arr:
        if x == 0:
            count += 1
    return count
"""),

    # =========================================================================
    # FALSE: Not clones — should be rejected
    # =========================================================================

    ("False", "Binary search vs fibonacci", 0,
     """\
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
""",
     """\
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
"""),

    ("False", "Bubble sort vs count pairs", 0,
     """\
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
""",
     """\
def count_pairs(arr, target):
    seen = {}
    count = 0
    for x in arr:
        if target - x in seen:
            count += seen[target - x]
        seen[x] = seen.get(x, 0) + 1
    return count
"""),

    ("False", "Formula vs nested loop", 0,
     """\
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32
""",
     """\
def max_subarray(arr):
    best = cur = arr[0]
    for x in arr[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
"""),

    ("False", "Factorial vs is_prime", 0,
     """\
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
""",
     """\
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
"""),

    ("False", "GCD vs two sum", 0,
     """\
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
""",
     """\
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []
"""),

    ("False", "Palindrome check vs bubble sort", 0,
     """\
def is_palindrome(s):
    lo, hi = 0, len(s) - 1
    while lo < hi:
        if s[lo] != s[hi]:
            return False
        lo += 1
        hi -= 1
    return True
""",
     """\
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
"""),

    ("False", "Fibonacci vs count pairs", 0,
     """\
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
""",
     """\
def count_pairs(arr, target):
    seen = {}
    count = 0
    for x in arr:
        if target - x in seen:
            count += seen[target - x]
        seen[x] = seen.get(x, 0) + 1
    return count
"""),

    ("False", "Linear search vs GCD", 0,
     """\
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
""",
     """\
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
"""),

    ("False", "Kadane vs is_prime", 0,
     """\
def max_subarray(arr):
    best = cur = arr[0]
    for x in arr[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
""",
     """\
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
"""),

    ("False", "Two sum vs factorial", 0,
     """\
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []
""",
     """\
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
"""),
]


# ── Evaluation ────────────────────────────────────────────────────────────────

def run():
    methods = available_methods()
    if not methods:
        print("No trained models found. Run train/main.py --save-models first.")
        return

    col_w = 15
    short_names = [m[:col_w - 1] for m in methods]

    header = f"{'Type':<8} {'Description':<38} {'Expected':<11}"
    for s in short_names:
        header += f" {s:<{col_w}}"
    print(header)
    print("-" * len(header))

    totals  = {m: {"correct": 0, "total": 0} for m in methods}
    by_type = {}

    for clone_type, desc, expected, func_a, func_b in TEST_CASES:
        label_str = "clone" if expected == 1 else "not clone"
        row = f"{clone_type:<8} {desc[:36]:<38} {label_str:<11}"

        if clone_type not in by_type:
            by_type[clone_type] = {m: {"correct": 0, "total": 0} for m in methods}

        for method in methods:
            try:
                label, score = predict(method, func_a, func_b)
                correct = (label == expected)
                mark = "PASS" if correct else "FAIL"
                cell = f"{mark}({score:.2f})"
                row += f" {cell:<{col_w}}"
                totals[method]["correct"] += correct
                totals[method]["total"]   += 1
                by_type[clone_type][method]["correct"] += correct
                by_type[clone_type][method]["total"]   += 1
            except Exception as e:
                row += f" {'ERR':<{col_w}}"

        print(row)

    # -- Overall accuracy
    print()
    print("-- Overall accuracy ------------------------------------------")
    for method, s in zip(methods, short_names):
        t = totals[method]
        pct = 100 * t["correct"] / t["total"] if t["total"] else 0
        print(f"  {s:<14}: {t['correct']:>2}/{t['total']} ({pct:.0f}%)")

    # -- Accuracy by clone type
    print()
    print("-- Accuracy by clone type ------------------------------------")
    for ct in ["Type-1", "Type-2", "Type-3", "Type-4", "False"]:
        if ct not in by_type:
            continue
        row = f"  {ct:<10}"
        for method, s in zip(methods, short_names):
            t = by_type[ct][method]
            pct = 100 * t["correct"] / t["total"] if t["total"] else 0
            row += f"  {s}: {t['correct']}/{t['total']} ({pct:.0f}%)"
        print(row)


if __name__ == "__main__":
    run()
