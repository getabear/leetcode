import functools
class Solution:
    # 别问我怎么做出来的,到现在题目都没看懂
    # 不过学到老functools
    @functools.lru_cache(None)   #可以记录最近调用的函数的返回值,如果是相等的参数,则会直接返回
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
                return True
            if self.isScramble(s1[:i],s2[-i:]) and self.isScramble(s1[i:],s2[:-i]):
                return True
        return False