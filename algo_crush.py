"""
HackerRank Algorithmic Crush problem:
https://www.hackerrank.com/challenges/crush

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
