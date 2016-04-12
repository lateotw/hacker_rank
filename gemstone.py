# 3
# abcdde
# baccd
# eeabg

n = int(input())
gemstone = set(input())

for i in range(n-1):
    gemstone = set.intersection(gemstone, set(input()))
print(len(gemstone))
