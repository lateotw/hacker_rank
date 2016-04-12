from builtins import hash



N = int(input())
t = tuple(map(int, input().split()))
print(hash(t))
