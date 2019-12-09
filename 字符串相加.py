class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def carry(nums):  # 处理进位
            # 举例：输入[15, 27, 12], 返回[5, 8, 4, 1]
            i = 0
            jin = 0
            size = len(nums)
            while (i < size):
                jin = nums[i] // 10
                if i == size - 1:  # 防止访问越界
                    if jin:
                        nums.append(jin)
                else:
                    nums[i + 1] += jin
                nums[i] %= 10
                i += 1
            return

        s1, s2 = num1, num2
        l1, l2 = len(s1), len(s2)
        if l1 < l2:
            s1, s2 = s2, s1
            l1, l2 = l2, l1
        s1 = [int(x) for x in s1]
        s2 = [int(x) for x in s2]
        s1, s2 = s1[::-1], s2[::-1]
        for i, digit in enumerate(s2):
            s1[i] += s2[i]

        carry(s1)
        s1 = s1[::-1]
        return "".join(str(x) for x in s1)