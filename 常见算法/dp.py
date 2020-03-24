# 使用递归方式实现斐波切纳数列, 不实用缓存直接递归的时间复杂度是O(2**n)
def rec_step(n, cache={}):
    if n not in cache:
        if n <= 2:
            cache[n] = n
        else:
            cache[n] = dp_fib(n - 1) + dp_fib(n - 2)
    return cache[n]


# 使用yield生成一个斐波切纳数列
def yield_fib(n):
    cnt, i, j = 0, 0, 1
    while cnt < n:
        yield j
        i, j = j, i + j
        cnt += 1


def test_yield_fib():
    res = []
    for elem in yield_fib(9):
        res.append(elem)
    assert res == [1, 1, 2, 3, 5, 8, 13, 21, 34]


test_yield_fib()


# 使用动态规划方式实现斐波切纳数列
def dp_fib(n):
    numbers = [None for _ in range(n + 1)]
    numbers[0], numbers[1], numbers[2] = 0, 1, 2
    for i in range(3, n + 1):
        numbers[i] = numbers[i - 1] + numbers[i - 2]
    return numbers[n]


"""
在一组数字中, 选择不相邻的数字, 使得其和为最大
如: [4, 1, 1, 9, 1], 其最大和为13。
"""


def rec_opt(arr, idx):
    if idx == 0:
        return arr[0]
    elif idx == 1:
        return max(arr[0], arr[1])
    else:
        select = rec_opt(arr, idx - 2) + arr[idx]
        not_select = rec_opt(arr, idx - 1)
        return max(select, not_select)


def test_rec_opt():
    arr = [4, 1, 1, 9, 1]
    assert rec_opt(arr, len(arr) - 1) == 13
    arr = [1, 2, 4, 1, 7, 8, 3]
    assert rec_opt(arr, len(arr) - 1) == 15


test_rec_opt()


def dp_opt(arr):
    length = len(arr)
    opt = [None] * length
    opt[0] = arr[0]
    opt[1] = max(arr[0], arr[1])
    for idx in range(2, length):
        opt[idx] = max(opt[idx - 2] + arr[idx], opt[idx - 1])
    return opt[length - 1]


def test_dp_opt():
    arr = [4, 1, 1, 9, 1]
    assert dp_opt(arr) == 13
    arr = [1, 2, 4, 1, 7, 8, 3]
    assert dp_opt(arr) == 15


test_dp_opt()

"""
从一组数字中, 是否存在一组数字的和为指定的数字, 如果存在, 返回True, 否则返回False。
如: [3, 34, 4, 12, 5, 2], 存在一组数字的和为9, 不存在一组数字的和为13。
"""


def rec_subset(arr, idx, target):
    if arr[idx] == target:
        return True
    elif idx == 0:
        return arr[0] == target
    # 如果当前的值已经比目标值大, 则不能再选当前值
    elif arr[idx] > target:
        return rec_subset(arr, idx - 1, target)
    else:
        select = rec_subset(arr, idx - 1, target - arr[idx])
        not_select = rec_subset(arr, idx - 1, target)
        return select or not_select


def test_rec_subset():
    arr = [3, 34, 4, 12, 5, 2]
    assert rec_subset(arr, len(arr) - 1, 9) is True
    arr = [3, 34, 4, 12, 5, 2]
    assert rec_subset(arr, len(arr) - 1, 10) is True
    arr = [3, 34, 4, 12, 5, 2]
    assert rec_subset(arr, len(arr) - 1, 11) is True
    arr = [3, 34, 4, 12, 5, 2]
    assert rec_subset(arr, len(arr) - 1, 12) is True
    arr = [3, 34, 4, 12, 5, 2]
    assert rec_subset(arr, len(arr) - 1, 13) is False


test_rec_subset()
