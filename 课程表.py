from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        length=len(prerequisites)
        if length==0:
            return True
        indegrees=[0 for i in range(numCourses)]
        adj=[set() for i in range(numCourses)]

        for seconed,first in prerequisites:
            indegrees[seconed]+=1
            adj[first].add(seconed)

        queue=deque()
        for i in range(numCourses):
            if indegrees[i]==0:
                queue.append(i)

        cnt=0
        while(queue):
            tmp=queue.popleft()
            cnt+=1
            for a in adj[tmp]:
                indegrees[a]-=1
                if indegrees[a]==0:
                    queue.append(a)
        return cnt==numCourses
