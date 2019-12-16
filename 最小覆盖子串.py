class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_t={}#记录t
        hash_w={}#记录windows

        #一次遍历t,时间复杂度O(M)假设t的长度为M
        for i in t:
            if i in hash_t:
                hash_t[i]+=1
            else:
                hash_t[i]=1
        #滑动窗口的开始和结束指针
        start=0
        end=0
        size_t=len(hash_t)
        match=0
        ret=s[:]+"1"
        while(end<len(s)):   #时间复杂度最多为O(N) 假设s的长度为N
            i=s[end]
            if i in hash_t:
                if i in hash_w:
                    hash_w[i]+=1
                else:
                    hash_w[i]=1
                if hash_w[i]==hash_t[i]:
                    match+=1
            if match==size_t:
                if end - start < len(ret):
                    ret = s[start:end + 1]
                while(1):
                    ch=s[start]
                    start += 1
                    if ch in hash_w:
                        hash_w[ch]-=1
                        if hash_w[ch]<hash_t[ch]:
                            match-=1
                            break
                    if end - start < len(ret):
                        ret = s[start:end + 1]
            end+=1
        return ret if len(ret)!=len(s)+1 else ""
    #总的时间复杂度为O(M+N)




a=Solution()
S = "ADOBECODEBANC"
T = "ABC"
print(a.minWindow(S,T))