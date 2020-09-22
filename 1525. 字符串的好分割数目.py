class Solution:
    def numSplits(self, s: str) -> int:
        mem1,mem2 = dict(),dict()
        ret = 0
        # 统计整个字符串某个字符的个数
        for i in s:
            try:
                mem1[i] += 1
            except:
                mem1[i] = 1
        for i in s:
            if i in mem2:
                mem2[i] += 1
            else:
                mem2[i] = 1
            if i in mem1:
                mem1[i] -= 1
                if mem1[i] == 0:
                    mem1.pop(i)
            if len(mem1) == len(mem2):
                ret += 1
        return ret

a=Solution()
s="acbadbaada"
print(a.numSplits(s))
