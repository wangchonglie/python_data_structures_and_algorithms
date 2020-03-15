"""
实现函数double Power(double base, int exponent):
"""
g_invalid_input = False


def power(base, exponent):
    global g_invalid_input

    if equal(base, 0.0) and exponent < 0:
        """
        避免底数为0且指数为负数的异常
        """
        g_invalid_input = True
        return 0.0
    abs_exponent = abs(exponent)
    result = powerhelper(base, abs_exponent)
    if exponent < 0:
        result = 1.0 / result
    print("result", result)
    return result


def equal(num1, num2):
    """
    float类型的数字在内存上不是精确的
    """
    if -0.0000001 < num2 - num1 < 0.0000001:
        return True
    else:
        return False


def powerhelper(base, abs_exponent):
    result = 1.0
    for i in range(1, abs_exponent + 1):
        result *= base
    return result


def test_power():
    base = 2
    exponent = 5
    assert power(base, exponent) == 32
    base = 2
    exponent = -5
    assert power(base, exponent) == 1 / 32
    base = -2
    exponent = -5
    assert power(base, exponent) == -1 / 32
    base = -2
    exponent = 5
    assert power(base, exponent) == -32
    base = 0
    exponent = 0
    # 0的0次方在数学上没有意义, 假定结果为1
    assert power(base, exponent) == 1


test_power()
