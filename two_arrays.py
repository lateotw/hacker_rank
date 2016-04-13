"""
https://www.hackerrank.com/challenges/two-arrays
"""

t = int(input())


def two_arr(N, K, A, B):

    if sum(A)+sum(B) < N * K:
        return 'NO'

    else:
        A.sort()
        B.sort(reverse=True)
        for i in range(N):
            if A[i] + B[i] < K:
                return 'NO'

    return 'YES'

for test in range(t):
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    print(two_arr(N, K, A, B))
