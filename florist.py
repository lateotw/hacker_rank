n, k = list(map(int, input().split()))  # n=number of flowers, k=people
cost = list(map(int, input().split()))  # cost of each flower

def price(n, k, cost):

    price = 0
    cost = sorted(cost, reverse=True)
    # print(cost)
    go_around = n // k  # go around the people

    for j in range(go_around):  # for each round j
        for people in range(k):
            price += cost[k * j + people] * (j+1)
            # if j == 0, people == 0, need cost[0] * 1
            # if j == 1, people == 0, need cost[people * j] * (1 + 1)

    # print(price)
    remaining = n % k           # and then the remaining

    # print(go_around, remaining)
    for j in range(remaining):
        # print(cost[go_around * k + j])
        price += cost[go_around * k + j] * (1 + go_around)
    return price

print(price(n, k, cost))
