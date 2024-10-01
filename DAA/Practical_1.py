# Practical 1
# Write a python program to calculate fibonacci numbers and find its step count

def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    count = 0

    for i in range(2, n + 1):
        a, b = b, a + b
        count += 1

    return a, count

def fibonacci_recursive(n):
    count = 0

    def fib(n):
        nonlocal count
        count += 1

        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    return fib(n), count

if __name__ == "__main__":
    n = int(input("Enter the value of n: "))

    fib_iterative, count_iterative = fibonacci_iterative(n)
    print("Fibonacci number (iterative):", fib_iterative)
    print("Step count (iterative):", count_iterative)

    fib_recursive, count_recursive = fibonacci_recursive(n)
    print("Fibonacci number (recursive):", fib_recursive)
    print("Step count (recursive):", count_recursive)

# Explanation of the program:
# This program calculates Fibonacci numbers and their step counts using both iterative and recursive approaches.
#
# 1. fibonacci_iterative(n):
#    - Implements an iterative approach to calculate the nth Fibonacci number.
#    - Uses two variables (a, b) to store the current and next Fibonacci numbers.
#    - Iterates n-1 times, updating a and b in each iteration.
#    - Returns the nth Fibonacci number and the step count.
#
# 2. fibonacci_recursive(n):
#    - Implements a recursive approach to calculate the nth Fibonacci number.
#    - Uses a nested function 'fib(n)' for the actual recursion.
#    - Increments a counter for each recursive call to track the step count.
#    - Returns the nth Fibonacci number and the total step count.
#
# 3. Main execution:
#    - Prompts the user to enter a value for n.
#    - Calls both fibonacci_iterative() and fibonacci_recursive() functions.
#    - Prints the calculated Fibonacci numbers and step counts for both approaches.
#
# The program demonstrates the difference in efficiency between iterative and recursive methods
# for calculating Fibonacci numbers, as reflected in their respective step counts.