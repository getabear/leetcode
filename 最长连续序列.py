from typing import List

class Solution1:
    #方法一:通过归并先进行排序,然后利用一次线性扫描记录最长连续子序列
    #归并排序时间复杂度O(nlogn)+线性扫描O(n)  总复杂度O(nlogn)
    #提交通过超越9.5%的用户
    def longestConsecutive(self, nums: List[int]) -> int:
        def merge(nums1,nums2):
            size1=len(nums1)
            index1=0
            size2=len(nums2)
            index2=0
            nums=[]
            while index1<size1 and index2<size2:
                if nums1[index1]<nums2[index2]:
                    nums.append(nums1[index1])
                    index1+=1
                else:
                    nums.append(nums2[index2])
                    index2+=1
            while index1<size1:
                nums.append(nums1[index1])
                index1+=1
            while index2<size2:
                nums.append(nums2[index2])
                index2+=1
            return nums
        def fun(nums: List[int]):
            size=len(nums)
            if size==1:
                return nums
            mid=size//2
            left=fun(nums[:mid])
            right=fun(nums[mid:])
            return merge(left,right)
        if nums:
            newnums=fun(nums)
        else:
            return 0
        ret=1
        i=0
        j=1
        size=len(newnums)
        tp=0
        while j<size:
            if newnums[i]+1==newnums[j]:
                tp+=1
                ret=max(ret,tp+1)
            elif newnums[i]!=newnums[j]:
                tp=0
            i+=1
            j+=1
        return ret
class Solution:
    # 时间复杂度：O(n)
    #尽管在for 循环中嵌套了一个 while 循环，时间复杂度看起来像是二次方级别的。
    # 但其实它是线性的算法。因为只有当 currentNum 遇到了一个序列的开始，
    # while 循环才会被执行（也就是 currentNum-1 不在数组 nums 里），
    # while 循环在整个运行过程中只会被迭代 nn 次。这意味着尽管看起来时间复杂度为 O(n⋅n) ，
    # 实际这个嵌套循环只会运行 O(n + n) = O(n)次.所有的计算都是线性时间的，所以总的时间复杂度是 O(n)的。

    def longestConsecutive(self, nums: List[int]) -> int:
        #来自官方解题:
        ret=0
        # set是一个无序且不重复的元素集合。
        # 集合对象是一组无序排列可哈希的值，集合成员可以做字典中的键。集合用in和not
        # in操作符检查成员，以len()
        # 內建函数得到集合的基数（大小），用for循环迭代集合的成员。但是因为集合本身是无序的，不可以为集合创建索引或执行切片(slice)
        # 操作，也没有键(keys)
        # 可用来获取集合中元素的值。
        # set和dict一样，只是没有value，相当于dict的key集合，由于dict的key是不重复的，且key是不可变对象因此set也有如下特性：
        #
        # 1.不重复
        # 2.元素为不可变对象
        num_set=set(nums)   #相当于建立一个hash表,可以快速检测一个数是否在num_set中
        for num in num_set:
            if num-1 not in num_set:   #说明这个数的前一个数没有,即证明了他是序列的开头
                current_num=num
                current=1
                while current_num+1 in num_set:  #如果这个数的后一个数存在,去找以他开头的数的长度
                    current_num+=1
                    current+=1
                ret=max(ret,current)        #维持最大长度的值
        return ret

a=Solution()
nums=[1,2,0,1]
print(a.longestConsecutive(nums))


