"""
请实现一个函数，输入一个整数，输出该数二进制表示中1的个数。例如把9表示成二进制是1001，有2位是1。因此如果输入9，该函数输出2。
"""


def method_1(num):
    count = 0
    flag = 1
    while flag:
        if num & flag:
            count += 1
        flag = flag << 1
        print(flag)
    return count


def method_2(num):
    count = 0
    while num:
        count += 1
        num = (num - 1) & num
    return count

print(method_1(9))
# print(method_2(9))
