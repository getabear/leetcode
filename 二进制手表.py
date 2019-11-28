class Solution(object):
    def __init__(self):
        self.result_all = None
        self.nums = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
        self.visited = None

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        self.result_all = []
        self.visited = [0 for _ in range(len(self.nums))]
        self.dfs(num, 0, 0)
        return self.result_all

    def dfs(self, num, step, start):
        if step == num:
            self.result_all.append(self.handle_date(self.visited))
            return
        for i in range(start, len(self.nums)):
            self.visited[i] = 1
            if not self.calc_sum(self.visited):
                self.visited[i] = 0
                continue
            self.dfs(num, step + 1, i + 1)
            self.visited[i] = 0
        return

    def calc_sum(self, visited):
        sum_h = 0
        sum_m = 0
        for i in range(len(visited)):
            if visited[i] == 0:
                continue
            if i < 4:
                sum_h += self.nums[i]
            else:
                sum_m += self.nums[i]
        return 0 <= sum_h <= 11 and 0 <= sum_m <= 59

    def handle_date(self, visited):
        sum_h = 0
        sum_m = 0
        for i in range(len(visited)):
            if visited[i] == 0:
                continue
            if i < 4:
                sum_h += self.nums[i]
            else:
                sum_m += self.nums[i]
        result = "" + str(sum_h) + ":"
        if sum_m < 10:
            result += "0" + str(sum_m)
        else:
            result += str(sum_m)
        return result


class Solution2(object):
    def __init__(self):
        self.result_all =[]
        self.nums = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]

    def readBinaryWatch(self, num):    #暴力穷举
        def count1(n):    #计算二进制中一的个数
            res = 0
            temp = 0
            # n=n&(n-1)
            # 这个表达式可以快速求出二进制中一的个数
            # 因为n-1影响最低位和他的借位的位置的二进制会导致他们与原位置不同
            # 相与就会导致最低位和借位位为零
            while n != 0:
                temp = n & 0x01
                n = n // 2
                res += temp

            return res
        count=0
        for i in range(12):
            for j in range(60):
                count+=count1(i)+count1(j)
                if count==num:
                    times=""+str(i)+":"
                    if j < 10:
                        times+="0"+str(j)
                    else:
                        times+=str(j)
                    self.result_all.append(times)
                times=""
                count=0
        return self.result_all


a=Solution2()
print(a.readBinaryWatch(1))

