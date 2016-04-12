def gift(b, w, x, y, z):
    if x > (y + z):
        money = b * (y + z) + w * y
    elif y > (x + z):
        money = b * x + w * (x + z)
    else:
        money = b * x + w * y
    return money


t = int(input().strip())
for a0 in range(t):
    b,w = input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    print(gift(b, w, x, y, z))
