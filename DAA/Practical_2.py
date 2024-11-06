# Practical 2
# Huffman Encoding Algorithm

import heapq

class MinHeapNode:
	def __init__(self, data, freq):
		self.data = data
		self.freq = freq
		self.left = None
		self.right = None

	def __lt__(self, other):
		return self.freq < other.freq

class HuffmanCoding:
	@staticmethod
	def print_codes(root, str_code):
		if root is None:
			return
		if root.data != '$':
			print(f"{root.data}: {str_code}")
		HuffmanCoding.print_codes(root.left, str_code + "0")
		HuffmanCoding.print_codes(root.right, str_code + "1")

	@staticmethod
	def huffman_code(data, freq):
		min_heap = []
		for i in range(len(data)):
			heapq.heappush(min_heap, MinHeapNode(data[i], freq[i]))

		while len(min_heap) > 1:
			left = heapq.heappop(min_heap)
			right = heapq.heappop(min_heap)
			temp = MinHeapNode('$', left.freq + right.freq)
			temp.left = left
			temp.right = right
			heapq.heappush(min_heap, temp)

		HuffmanCoding.print_codes(min_heap[0], "")

def main():
	data = ['A', 'B', 'C', 'D' , 'E', 'F']
	freq = [23, 12, 34, 10,5,123 ]
	HuffmanCoding.huffman_code(data, freq)

if __name__ == "__main__":
	main()

"""
Explanation:

This code implements the Huffman Encoding Algorithm, which is used for lossless data compression. The algorithm assigns variable-length codes to characters based on their frequencies, with more frequent characters getting shorter codes.

Key components:
1. MinHeapNode: Represents a node in the Huffman tree, containing character data, frequency, and left/right child nodes.
2. HuffmanCoding: Contains static methods for building the Huffman tree and printing the codes.
3. huffman_code: Builds the Huffman tree using a min-heap and generates the codes.
4. print_codes: Recursively traverses the Huffman tree to print the codes for each character.

Example Input:
data = ['A', 'B', 'C', 'D']
freq = [23, 12, 34, 10]

Example Output:
C: 0
D: 100
A: 101
B: 111

The output shows the Huffman codes assigned to each character based on their frequencies.

Space Complexity:
O(n), where n is the number of unique characters. The space is used to store the min-heap and the Huffman tree.

Time Complexity:
O(n log n), where n is the number of unique characters.
- Building the initial min-heap: O(n)
- Main loop (creating the Huffman tree): O(n log n), as we perform n-1 extract-min and insert operations on the heap
- Printing the codes: O(n), as we traverse each node once

The dominant factor is the main loop, so the overall time complexity is O(n log n).
"""
