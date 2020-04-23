from typing import List
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses==0:
            return []
        adj=[set() for i in range(numCourses)]    #用来记录某个节点的后继节点
        indegrees=[0 for i in range(numCourses)]  #记录某个节点的入度
        for sec,fir in prerequisites:
            indegrees[sec]+=1
            adj[fir].add(sec)
        queue=deque()
        for index,i in enumerate(indegrees):
            if i==0:   #将入度为0 的节点加入双端队列
                queue.append(index)

        res=[]
        while queue:
            tmp=queue.popleft()
            res.append(tmp)
            for i in adj[tmp]:
                indegrees[i]-=1
                if indegrees[i]==0:
                    queue.append(i)
        return res if len(res)==numCourses else []