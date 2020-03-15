def rec_step(n, cache={}):
    if n not in cache:
        if n <= 2:
            cache[n] = n
        else:
            cache[n] = dp_step(n - 1) + dp_step(n - 2)
    return cache[n]


def dp_step(n):
    ways = [i for i in range(n + 1)]
    ways[0], ways[1], ways[2] = 0, 1, 2
    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]
    return ways[n]
print(dp_step(10))
