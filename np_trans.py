import numpy as np

n, m = list(map(int, input().split()))
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

arr = np.reshape(np.array(arr), [n, m])

print(arr.transpose())
print(arr.flatten())
