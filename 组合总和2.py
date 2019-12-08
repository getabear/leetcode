from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret=[]
        def fun(candidates,target,result,start):
            if target==0:
                if result not in ret:
                    ret.append(result[:])
                return
            for index in range(len(candidates)):
                if candidates[index] > target:   #第二次直接减枝操作,大幅减少时间的消耗
                    break
                if index>start:
                    result.append(candidates[index])
                    fun(candidates,target-candidates[index],result,index)
                    result.remove(candidates[index])
            return
        # def fun(candidates,target,result,start):
        #     if target==0:
        #         if result not in ret:
        #             ret.append(result[:])
        #         return
        #     if target<0:    #第一次这样写,时间消耗多很多
        #         return
        #     for index in range(len(candidates)):
        #         if index>start:
        #             result.append(candidates[index])
        #             fun(candidates,target-candidates[index],result,index)
        #             result.remove(candidates[index])
        #     return
        candidates.sort()
        fun(candidates,target,[],-1)
        return ret

a=Solution()
candidates = [2,5,2,1,2]
target = 5
print(a.combinationSum2(candidates,target))