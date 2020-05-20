class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def fun(s,k):
            if len(s)<k:
                return 0
            mem=dict()
            for i in s:
                if i in mem:
                    mem[i]+=1
                else:
                    mem[i]=1
            min_conut=len(s)
            for i in mem.keys():
                if min_conut>=mem[i]:
                    min_conut=mem[i]
                    key=i
            if min_conut>=k:
                return len(s)
            max_len=0
            for T in s.split(key):
                max_len=max(max_len,fun(T,k))
            return max_len
        return fun(s,k)
s="bbaaacbd"
k=3
a=Solution()
print(a.longestSubstring(s,k))