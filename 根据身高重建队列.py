from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:x[1])
        nums={}
        for i in people:
            try:
                nums[i[1]].append(i)
            except:
                nums[i[1]]=[]
                nums[i[1]].append(i)
        ret=[]
        for key,val in nums.items():
            val.sort(key=lambda x:x[0])
            for v in val:
                index,cnt=0,0
                flag=1
                while index<len(ret):
                    if ret[index][0]>=v[0]:
                        cnt+=1
                    if cnt==key+1:
                        ret.insert(index,v)
                        flag-=1
                        break
                    index+=1
                if flag:
                    ret.append(v)
        return ret

people=[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
a=Solution()
print(a.reconstructQueue(people))