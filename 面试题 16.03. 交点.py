from typing import List

class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        x1,y1=start1[0],start1[1]
        x2,y2=end1[0],end1[1]

        x3,y3=start2[0],start2[1]
        x4,y4=end2[0],end2[1]
        if(x1<x2):
            tmp1=x2
        else:
            tmp1=x1
        if(x3<x4):
            tmp2=x3
        else:
            tmp2=x4
        if(tmp1<tmp2):
            return []
        if(y1<y2):
            tmp1=y2
        else:
            tmp1=y1
        if(y3<y4):
            tmp2=y3
        else:
            tmp2=y4
        if(tmp1<tmp2):
            return []


        k1=float("inf")
        k2=float("inf")

        if(x2-x1!=0):
            k1=(y2-y1)/(x2-x1)
        if(x4-x3!=0):
            k2=(y4-y3)/(x4-x3)

        if(k1==k2):   #如果平行
            if(k1!=float("inf")):
                b1 = y1 - k1 * x1
                b2 = y3 - k2 * x3
                if(b1==b2):
                    x_list=[x1,x2,x3,x4]
                    x=min(x1,x2,x3,x4)
                    x_list.remove(x)
                    x=min(x_list)
                    y=k1*x+b1
                    return [x,y]
                else:
                    return []
            else:
                if(x1!=x3):
                    return []
                else:
                    x_list=[x1,x2,x3,x4]
                    y_list=[y1,y2,y3,y4]
                    x=0
                    xx=0
                    for i in range(4):
                        if x_list[i]<x_list[x]:
                            x=i
                    for i in range(4):
                        if i==x:
                            continue
                        if x_list[i]<x_list[xx]:
                            xx=i
                    return [x_list[xx],y_list[xx]]

        else: #不平行
            if(k1!=float("inf") and k2!=float("inf")):
                b1 = y1 - k1 * x1
                b2 = y3 - k2 * x3
                x=(b2-b1)/(k1-k2)
                if(x>=min(x1,x2) and x<=max(x1,x2) and x>=min(x3,x4) and x<=max(x3,x4)):
                    y=k1*x+b1
                    return [x,y]
                return []
            if(k1==float("inf")):
                b2 = y3 - k2 * x3
                x=x1
                y=k2*x1+b2
                return [x,y]
            if (k2 == float("inf")):
                b1 = y1 - k1 * x1
                x=x2
                y=k1*x+b1
                return [x,y]


a=Solution()




start1=[1,1]
end1=[-1,1]
start2=[1,0]
end2=[-3,2]
print(a.intersection(start1,end1,start2,end2))
