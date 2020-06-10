from typing import List

class UF:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
    def find(self,x):
        while x!=self.parent[x]:
            x=self.parent[x]
        return x

    def union(self,x,y):
        root_x=self.find(x)
        root_y=self.find(y)
        self.parent[root_x]=root_y

    def connect(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        return root_x==root_y

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        unionFind=UF(26)
        for equation in equations:
            if equation[1]=='=':
                index1=ord(equation[0])-ord('a')
                index2=ord(equation[-1])-ord('a')
                unionFind.union(index1,index2)
        for equation in equations:
            if equation[1]=='!':
                index1=ord(equation[0])-ord('a')
                index2=ord(equation[-1])-ord('a')
                if unionFind.connect(index1,index2):
                    return False
        return True

a=Solution()
equations=["a==b","b!=c","c==a"]
print(a.equationsPossible(equations))


