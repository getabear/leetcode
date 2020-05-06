class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        mem1=dict()
        mem2=dict()
        for i in s:
            if i in mem1:
                mem1[i]+=1
            else:
                mem1[i]=1
        for i in t:
            if i in mem2:
                mem2[i]+=1
            else:
                mem2[i]=1
        return mem1==mem2

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mem = dict()
        for i in s:
            if i in mem:
                mem[i] += 1
            else:
                mem[i] = 1
        for i in t:
            if i not in mem:
                return False
            else:
                mem[i]-=1
                if mem[i]==0:
                    mem.pop(i)
        return mem=={}