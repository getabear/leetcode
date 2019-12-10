from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #暴力法,有问题,懒得找了
        ret=[]
        def dif(str1,str2):
            if(len(str1)!=len(str2)):
                return False
            for i in str1:
                if i in str2:
                    continue
                else:
                    return False
            for i in str2:
                if i in str1:
                    continue
                else:
                    return False
            return True
        def fun(strs):
            for i in strs:
                flag=0
                for j in ret:
                    if dif(j[0],i):
                        j.append(i)
                        flag=1
                        break
                if flag==0:
                    ret.append([i])
            return ret
        return fun(strs)

class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #超时
        ret=[]
        for i in strs:
            tp=list(i)
            tp.sort()
            flag=0
            for j in ret:
                temp=list(j[0])
                temp.sort()
                if  temp==tp:
                    j.append(i)
                    flag=1
                    break
            if flag==0:
                ret.append([i])
        return ret
class Solution3:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        lookup = defaultdict(list)
        for s in strs:
            lookup["".join(sorted(s))].append(s)
        return list(lookup.values())

a=Solution1()
strs=["ca","ca"]
print(a.groupAnagrams(strs))