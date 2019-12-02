class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map={}
        ret=0
        start=0  #开始下标
        # length=0
        if not s:
            return ret
        for index,i in enumerate(s):
            if hash_map.get(i) is not None:
                if hash_map.get(i)>=start: #如果出现在start后,则有效,更新返回值
                    ret=max(index-start,ret)
                    start=hash_map.get(i)+1   #并且更新下标
            hash_map[i]=index
        ret=max(index-start+1,ret)
        return ret

a=Solution()
s=""
print(a.lengthOfLongestSubstring(s))
