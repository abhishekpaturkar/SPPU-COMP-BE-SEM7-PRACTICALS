# Practical 3
# Write a program to solve a fractional Knapsack problem using greedy method

def fractional_knapsack_by_ratio(items, capacity):
	sorted_items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)    
	total_value = 0
	
	for value, weight in sorted_items:
		if capacity >= weight:
			total_value += value
			capacity -= weight
		else:
			total_value += capacity * (value / weight)
			break
	
	return total_value

def fractional_knapsack_by_weight(items, capacity):
	sorted_items = sorted(items, key=lambda x: x[1])    
	total_value = 0
	
	for value, weight in sorted_items:
		if capacity >= weight:
			total_value += value
			capacity -= weight
		else:
			total_value += capacity * (value / weight)
			break
	
	return total_value

def fractional_knapsack_by_value(items, capacity):
	sorted_items = sorted(items, key=lambda x: x[0], reverse=True)    
	total_value = 0
	
	for value, weight in sorted_items:
		if capacity >= weight:
			total_value += value
			capacity -= weight
		else:
			total_value += capacity * (value / weight)
			break
	
	return total_value

def main():
	items = [[60, 10], [100, 20], [120, 30]]  # Different values for different results
	capacity = 50
	
	max_value_ratio = fractional_knapsack_by_ratio(items, capacity)
	max_value_weight = fractional_knapsack_by_weight(items, capacity)
	max_value_value = fractional_knapsack_by_value(items, capacity)
	
	print(f"Maximum value by value/weight ratio: {max_value_ratio:.2f}")
	print(f"Maximum value by weight: {max_value_weight:.2f}")
	print(f"Maximum value by value: {max_value_value:.2f}")

if __name__ == "__main__":
	main()		


"""
Fractional Knapsack Problem:
The fractional knapsack problem is an optimization problem where we need to fill a knapsack with items to maximize the total value, but we can take fractions of items. Each item has a weight and a value. Unlike the 0/1 knapsack problem, we can break items into smaller units to maximize the total value in the knapsack.

Example:
Consider a knapsack with a capacity of 50 kg and the following items:
1. Gold: 20 kg, $100
2. Silver: 30 kg, $90
3. Bronze: 10 kg, $60

Solution:
1. Take all 20 kg of Gold: 20 kg, $100
2. Take all 10 kg of Bronze: 30 kg, $160
3. Take 20 kg of Silver (2/3 of it): 50 kg, $160 + $60 = $220

The maximum value we can achieve is $220 by filling the knapsack with 20 kg of Gold, 10 kg of Bronze, and 20 kg of Silver.

This code solves the fractional knapsack problem using a greedy approach. It sorts items by value-to-weight ratio, then adds items to the knapsack, taking fractions if needed.

Time complexity: O(n log n) due to sorting, where n is the number of items
Space complexity: O(1) as we're using a constant amount of extra space
"""