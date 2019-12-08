from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret=[]
        candidates.sort()
        def fun(result,target,temp):
            if target==0:
                if result not in ret:
                    # 这里一定要用result[:],不然result改变了,ret也变了
                    # Python中可变对象是引用传递，因此需要将当result里的值拷贝出来
                    #这里把我坑舒服了,我调试了半天才发现这个问题
                    ret.append(result[:])
                return
            if target<0:
                return
            for i in candidates:
                if i>=temp:
                    result.append(i)
                    fun(result,target-i,i)
                    result.pop()
            return
        fun([],target,0)
        return ret

a=Solution()
candidates=[2,2,3,7]
target=7
print(a.combinationSum(candidates,target))