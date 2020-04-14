from typing import List

class Solution1:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        #穷举法超时了
        def fun(s,des):
            if len(s)<10:
                return False
            if s[:10]==des:
                return True
            return fun(s[1:],des)

        ret=[]
        for i in range(len(s)-9):
            des=s[i:i+10]
            if(des not in ret):
                if(fun(s[i + 1:], des)):
                    ret.append(des)

        return ret

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        #利用hash表,提交后通过了测试用例
        output=set()
        hash=set()
        for i in range(len(s)-9):
            tmp=s[i:i+10]
            if tmp in hash:
                output.add(tmp)
            else:
                hash.add(tmp)
        return list(output)
a=Solution()
s="AAAAAAAAAAA"
print(a.findRepeatedDnaSequences(s))


