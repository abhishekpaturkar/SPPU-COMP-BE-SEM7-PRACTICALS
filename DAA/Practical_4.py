# Practical 4
# Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and bound strategy

# Dynamic Programming Approach
def knapsack_dp(price, wt, items, capacity):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(items + 1)]
    
    for i in range(1, items + 1):
        for w in range(1, capacity + 1):
            if wt[i] <= w:
                dp[i][w] = max(price[i] + dp[i-1][w-wt[i]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[items][capacity]

# Branch and Bound Approach
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def knapsack_branch_and_bound(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    n = len(items) - 1  # Adjusting for 1-based indexing
    
    def bound(node, k, current_weight, current_value):
        if current_weight >= capacity:
            return 0
        bound_value = current_value
        total_weight = current_weight
        for i in range(k, n + 1):
            if total_weight + items[i].weight <= capacity:
                bound_value += items[i].value
                total_weight += items[i].weight
            else:
                bound_value += (capacity - total_weight) * items[i].ratio
                break
        return bound_value
    
    def knapsack_recursive(k, current_weight, current_value):
        nonlocal max_value
        if k == n + 1:
            max_value = max(max_value, current_value)
            return
        
        if current_weight + items[k].weight <= capacity:
            if bound(items[k], k + 1, current_weight + items[k].weight, current_value + items[k].value) > max_value:
                knapsack_recursive(k + 1, current_weight + items[k].weight, current_value + items[k].value)
        
        if bound(items[k], k + 1, current_weight, current_value) > max_value:
            knapsack_recursive(k + 1, current_weight, current_value)
    
    max_value = 0
    knapsack_recursive(1, 0, 0)
    return max_value

# Example usage
if __name__ == "__main__":
    capacity = 10
    items = 4
    price = [0, 3, 7, 2, 9]
    wt = [0, 2, 2, 4, 5]
    dp = [[0 for _ in range(capacity + 1)] for _ in range(items + 1)]

    print("Dynamic Programming Approach:")
    print("Maximum value:", knapsack_dp(price, wt, items, capacity))

    print("\nBranch and Bound Approach:")
    item_objects = [Item(0, 0)] + [Item(w, v) for w, v in zip(wt[1:], price[1:])]
    print("Maximum value:", knapsack_branch_and_bound(item_objects, capacity))

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
