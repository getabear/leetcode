from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:   #这道题的优化可以改为先找到最短的字符串,然后遍历
        num_of_str=len(strs)
        if (num_of_str==0):
            return ''
        cur=1
        ret=''
        for index,i  in enumerate(strs[0]):
            while(cur<num_of_str):
                if(index==len(strs[cur]) or i!=strs[cur][index]):
                    return ret
                cur+=1
            cur=1
            ret+=i
        return ret

a=Solution()
s=[]
print(a.longestCommonPrefix(s))
