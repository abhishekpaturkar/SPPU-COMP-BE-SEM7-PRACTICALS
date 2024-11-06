# Practical 4
# Write a program to solve a 0-1 Knapsack problem using dynamic programming.

# Dynamic Programming Approach
def knapsack_01(n, values, weights, W):
    # Create a 2D DP table initialized with zeros
    dp = [[0] * (W+1) for _ in range(n+1)]

    # Fill the DP table
    for i in range(n+1):
        for w in range(W+1):
            # Base case: no items or no capacity
            if i == 0 or w == 0:
                dp[i][w] = 0
            # If current item's weight can fit in the knapsack
            elif weights[i-1] <= w:
                # Take maximum of including or excluding current item
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            # If current item's weight exceeds capacity
            else:
                # Exclude current item
                dp[i][w] = dp[i-1][w]
    
    # Backtrack to find selected items
    selected_items = []
    i, w = n, W
    while i > 0 and w > 0:
        # If current item was included
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
        i -= 1
    
    # Return maximum value and list of selected items
    return dp[n][W], selected_items

if __name__ == "__main__":
    # Test case
    n = 3  # Number of items
    values = [60, 100, 120]  # Values of items
    weights = [10, 20, 30]   # Weights of items
    W = 50  # Knapsack capacity

    # Solve the knapsack problem
    max_value, selected_items = knapsack_01(n, values, weights, W)
    print("Maximum value:", max_value)
    print("Selected items:", selected_items)

"""
Explanation of the 0-1 Knapsack Problem:

The 0-1 Knapsack problem is an optimization problem where we have a set of items, each with a weight and a value, and we need to determine which items to include in a collection (knapsack) so that the total weight is less than or equal to a given limit (capacity) and the total value is as large as possible.

In this example:
- We have 4 items with weights [2, 2, 4, 5] and corresponding values [3, 7, 2, 9].
- The knapsack capacity is 10.

Dynamic Programming Approach:
The DP approach builds a table (dp) where dp[i][w] represents the maximum value that can be achieved with the first i items and a capacity of w. It fills this table iteratively, considering whether to include or exclude each item.

Branch and Bound Approach:
This approach uses a tree structure where each node represents a decision to include or exclude an item. It uses a bounding function to prune branches that cannot lead to an optimal solution, thus reducing the search space.

Complexity:
1. Dynamic Programming:
   - Time Complexity: O(n * W), where n is the number of items and W is the capacity.
   - Space Complexity: O(n * W) for the DP table.

2. Branch and Bound:
   - Time Complexity: O(2^n) in the worst case, but typically much better in practice due to pruning.
   - Space Complexity: O(n) for the recursion stack.

Which is better?
The choice between DP and Branch and Bound depends on the problem instance:

1. Dynamic Programming is generally preferred for smaller to medium-sized problems. It has a predictable runtime and is easier to implement.

2. Branch and Bound can be more efficient for larger problems, especially when good bounds can be established quickly. It can potentially solve the problem faster by pruning large portions of the search space.

In practice, Dynamic Programming is often the go-to method for the 0-1 Knapsack problem due to its simplicity and predictable performance. However, for very large instances or when memory is a constraint, Branch and Bound might be more suitable.
"""
