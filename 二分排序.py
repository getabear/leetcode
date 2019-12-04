def hebing(nums1,nums2):
    len1=len(nums1)
    len2=len(nums2)
    i1,i2=0,0
    nums=[]
    while(i1<len1 and i2<len2):
        if(nums1[i1]>nums2[i2]):
            nums.append(nums2[i2])
            i2+=1
        else:
            nums.append(nums1[i1])
            i1+=1
    if(i1<len1):
        while(i1<len1):
            nums.append(nums1[i1])
            i1+=1
        return nums
    else:
        while(i2<len2):
            nums.append(nums2[i2])
            i2+=1
        return nums


def paixu(nums):
    length=len(nums)
    mid=length//2
    if(length==1):
        return nums[:]
    else:
        lefts=paixu(nums[0:mid])
        rights=paixu(nums[mid:length])
        num=hebing(lefts,rights)
        return num[:]

nums=[213,34,1,3123,1,123,13,123]

nums=paixu(nums)
length=len(nums)
print(nums)
print(nums[length//2])






