"""
去除有序数组的重复元素
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
示例一:
给定数组 nums = [1,1,2],
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
你不需要考虑数组中超出新长度后面的元素。
示例二:
给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。
"""

"""
解决思路:
由于数组已经排序，所以重复的元素一定连在一起，找出它们并不难，但如果毎找到一个重复元素就立即删除它，就是在数组中间进行删除操作，整个时间复杂度
是会达到 O(N^2)。而且题目要求我们原地修改，也就是说不能用辅助数组，空间复杂度得是 O(1)。

其实，对于数组相关的算法问题，有一个通用的技巧：要尽量避免在中间删除元素，那我就想先办法把这个元素换到最后去。这样的话，最终待删除的元素都拖在
数组尾部，一个一个 pop 掉就行了，每次操作的时间复杂度也就降低到 O(1) 了。

按照这个思路呢，又可以衍生出解决类似需求的通用方式：双指针技巧。具体一点说，应该是快慢指针。
我们让慢指针 slow 走左后面，快指针 fast 走在前面探路，找到一个不重复的元素就告诉 slow 并让 slow 前进一步。这样当 fast 指针遍历完整个数组
nums 后，nums[0..slow] 就是不重复元素，之后的所有元素都是重复元素。
"""


def remove_duplicates(nums):
    length = len(nums)
    if length == 0:
        return 0
    slow = 0
    fast = 1
    while fast < length:
        if nums[fast] != nums[slow]:
            slow += 1
            # 维护 nums[0...slow] 无重复
            nums[slow] = nums[fast]
        fast += 1
    # 长度为索引 + 1
    return slow + 1


def test_remove_duplicates():
    seq = [1, 1, 2]
    assert remove_duplicates(seq) == 2
    seq = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert remove_duplicates(seq) == 5
    seq = []
    assert remove_duplicates(seq) == 0
    seq = [1, 1]
    assert remove_duplicates(seq) == 1


test_remove_duplicates()

"""
简单扩展一下，如果给你一个有序链表，如何去重呢？其实和数组是一模一样的，唯一的区别是把数组赋值操作变成操作指针而已
"""


def delete_duplicates(head):
    if head is None:
        return None
    slow = head
    fast = head.next
    while fast is not None:
        if fast.val != slow.val:
            # slow += 1
            slow = slow.next
            # nums[slow] = nums[fast]
            slow.next = fast
        fast = fast.next
    # 断开与后面重复元素的连接
    slow.next = None
    return head


"""
82题: 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:
1. 必须在原数组上操作，不能拷贝额外的数组。
2. 尽量减少操作次数。
"""


def move_0_end(array):
    slow = 0
    fast = 0
    length = len(array)
    while fast < length:
        if array[slow] != 0:
            slow += 1
        elif array[fast] != 0:
            array[slow], array[fast] = array[fast], array[slow]
            slow += 1
        fast += 1
    return array


def test_move_0_end():
    t1 = [0, 1, 0, 3, 12]
    assert move_0_end(t1) == [1, 3, 12, 0, 0]


test_move_0_end()

"""
LeetCode: 5.寻找最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"
"""


def palindrome(string, left, right):
    length = len(string)
    while left >= 0 and right < length and string[left] == string[right]:
        left -= 1
        right += 1
    return string[left + 1: right]


def longest_palindrome(string):
    res = ''
    for i in range(len(string)):
        # 以 string[i] 为中心的最长回文子串
        s1 = palindrome(string, i, i)
        # 以 string[i], string[i+1] 为中心的最长回文子串
        s2 = palindrome(string, i, i + 1)
        res = res if len(res) > len(s1) else s1
        res = res if len(res) > len(s2) else s2
    print(res)
    return res


def test_longest_palindrome():
    s = 'babad'
    assert longest_palindrome(s) == 'aba'
    s = 'cbbd'
    assert longest_palindrome(s) == 'bb'


test_longest_palindrome()
