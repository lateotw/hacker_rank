
m = int(input())
M = set(list(map(int, input().split())))
n = int(input())
N = set(list(map(int, input().split())))
M_or_N = sorted(M.union(N))
M_and_N = M.intersection(N)

for i in M_and_N:
    M_or_N.remove(i)

for i in M_or_N:
    print(i)
