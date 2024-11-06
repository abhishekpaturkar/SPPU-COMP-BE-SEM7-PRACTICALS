import time
import tracemalloc
import gc

# Recursive Fibonacci
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Iterative (Non-Recursive) Fibonacci
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Function to calculate and print time and approximate memory complexity
def analyze_fibonacci(n):
    # Recursive Fibonacci with time and memory measurement
    gc.collect()  # Force garbage collection before starting
    tracemalloc.start()  # Start memory tracking
    start_time = time.perf_counter()
    result_recursive = fibonacci_recursive(n)
    end_time = time.perf_counter()
    recursive_time = end_time - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f"Fibonacci of {n} (Recursive): {result_recursive}")
    print(f"Time taken (Recursive): {recursive_time:.6f} seconds")
    print(f"Peak memory usage (Recursive): {peak / 1024:.2f} KB\n")

    # Iterative Fibonacci with time and memory measurement
    gc.collect()  # Force garbage collection before starting
    tracemalloc.start()  # Start memory tracking
    start_time = time.perf_counter()
    result_iterative = fibonacci_iterative(n)
    end_time = time.perf_counter()
    iterative_time = end_time - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Fibonacci of {n} (Iterative): {result_iterative}")
    print(f"Time taken (Iterative): {iterative_time:.6f} seconds")
    print(f"Peak memory usage (Iterative): {peak / 1024:.2f} KB")

# Example usage with a higher value of n
n = 30
analyze_fibonacci(n)

