from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #咱们先用穷举法试试,提交后超时,很显然算法是对的,但是算法复杂度较高,O(n^2)
        # 咱们想想怎么优化吧!!!
        size=len(gas)
        residue=0  #剩余的油量
        start=0
        while(start<size):
            if gas[start]>=cost[start]:
                residue=gas[start]-cost[start]
                if start+1<size:
                    index=start+1
                else:
                    index=0
                while residue>=0:
                    residue+=gas[index]
                    residue-=cost[index]
                    if index==start:
                        return start
                    index+=1
                    if index==size:
                        index=0
            start+=1
        return -1

class Solution1:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        size=len(gas)
        residue=0  #剩余的油量
        res=0
        total=0
        start=0
        while(start<size):
            total+=gas[start]-cost[start]   #要能转一圈,必须总和大于0
            if residue<0:
                residue=gas[start]-cost[start]
                res=start
            else:
                residue+=gas[start]-cost[start]
            start+=1
        return res if total>=0 else -1


a=Solution1()
gas  = [3,3,4]
cost =[3,4,4]
print(a.canCompleteCircuit(gas,cost))
# KeyError: 2
# Line 16 in canCompleteCircuit (Solution.py)
# Line 52 in _driver (Solution.py)
# Line 65 in <module> (Solution.py)