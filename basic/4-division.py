# Task: The provided code stub reads two integers, a and b, from STDIN.
# Add logic to print two lines.
# The first line should contain the result of integer division,
# The second line should contain the result of float division,
# No rounding or formatting is necessary.
# Example: a=3, b=5
# The result of the integer division is 0
# The result of the float division is 0.6
# Input Format: The first line contains the first integer,
#               The second line contains the second integer,
# Output Format: Print the two lines as described above.
# Sample Input: 4, 3
# Sample Output:1, 1.33333

a = int(input())
b = int(input())
print(a//b)
print(a/b)
