from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        size=len(buildings)
        if size==0:
            return []
        if size==1:
            x,x_end,high=buildings[0]
            return [[x,high],[x_end,0]]
        left_sky=self.getSkyline(buildings[:size//2])
        right_sky=self.getSkyline(buildings[size//2:])
        return self.mergeSkyline(left_sky,right_sky)

    def mergeSkyline(self,left_sky,right_sky):
        output=[]   #用以存储天际线结果
        def update(x,y):
            if not output or output[-1][0]!=x:
                output.append([x,y])
            else:
                output[-1][1]=y

        def append_skyline(p,lst,n,cur_y):
            while p<n:
                x,y=lst[p]
                p+=1
                if y!=cur_y:
                    update(x,y)
                    cur_y=y

        left_n=len(left_sky)
        right_n=len(right_sky)
        left_p,right_p=0,0   #初始化左右指针
        cur_y,left_y,right_y=0,0,0
        while left_p<left_n and right_p<right_n:
            left_point,right_point=left_sky[left_p],right_sky[right_p]
            if left_point[0]<right_point[0]:    #找到左右指针的最小x
                x,left_y=left_point
                left_p+=1
            else:
                x,right_y=right_point
                right_p+=1
            maxy=max(left_y,right_y)
            if cur_y!=maxy:
                update(x,maxy)
                cur_y=maxy

        #处理前面为处理完的左或者右天际线
        append_skyline(left_p,left_sky,left_n,cur_y)
        append_skyline(right_p,right_sky,right_n,cur_y)

        return output

