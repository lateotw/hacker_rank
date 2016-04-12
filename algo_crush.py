"""
HackerRank Algorithmic Crush problem

You are given a list of size NN, initialized with zeroes. You have to perform MM operations on the list and output the maximum of final values of all the NN elements in the list. For every operation, you are given three integers aa, bb and kk and you have to add value kk to all the elements ranging from index aa to bb(both inclusive).

Input Format
First line will contain two integers NN and MM separated by a single space.
Next MM lines will contain three integers aa, bb and kk separated by a single space.
Numbers in list are numbered from 11 to NN.

Output Format
A single line containing maximum value in the updated list.
"""


n, m = list(map(int, input().split()))  # n elements, m test cases

my_list = [0] * (n+1)
max_number = 0
x = 0

for i in range(m):
    a, b, k = list(map(int, input().split()))
    my_list[a-1] += k
    my_list[b] -= k

for j in range(n):
    x += my_list[j]
    if max_number < x:
        max_number = x

print(max_number)

