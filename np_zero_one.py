import numpy as np

n = list(map(int, input().split()))
ar_shape = n[0],

if len(n) > 1:
    for i in range(1, len(n)):
        ar_shape = ar_shape + (n[i],)

print(np.zeros((ar_shape), dtype=np.int))
print(np.ones((ar_shape), dtype=np.int))
