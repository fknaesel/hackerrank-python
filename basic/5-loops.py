# Task: The provided code stub reads and integer, n, from STDIN.
# For all non-negative integers i < n, print i²
# Example: 3 -> [0,1,2] -> [0,1,4]
# Input Format: The first and only line contains the integer, n
# Constraints: 1 <= n <= 20
# Output Format: Print n lines, one corresponding to each i
# Sample Input: 5
# Sample Output: 0, 1, 4, 9, 16

n = int(input().strip())
for i in range(0,n):
    print(i**2)
