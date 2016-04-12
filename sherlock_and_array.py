def find_pivot(ar):
    find = 'NO'

    if len(ar) > 2:

        index = 1
        left = ar[0]
        right = sum(ar[(index+1):])

        while (find == 'NO') & (index < len(ar)-1):
            if left == right:
                find = 'YES'
            left += ar[index]
            right -= ar[index+1]
            index += 1

    return find


test_cases = int(input())

for i in range(test_cases):
    arr_length = int(input())
    arr = list(map(int, input().split()))
    if arr_length == 1:
        print('YES')
    else:
        print(find_pivot(arr))

# print(find_pivot([1, 2, 3]))
# 2
# 3
# 1 2 3
# 4
# 1 2 3 3
