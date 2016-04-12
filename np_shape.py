import numpy as np

arr = list(map(int, input().split()))
arr = np.reshape(np.array(arr), (3,3))
print(arr)
