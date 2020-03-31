# url:https://yq.aliyun.com/articles/681640

class HeapSort:
    def build(self,arr,parent,length):
        #参数说明 :arr 数组     parent:父节点小标    length:数组长度
        i=2*parent    #子节点的小标计算    (参考完全二叉树)
        while i<length:
            if i+1<length and arr[i]<arr[i+1]:   #找出父节点的最大子节点   i+1为父节点的右子节点
                i+=1
            if arr[parent]>arr[i]:  #如果父节点比子节点大  直接退出循环
                break
            arr[parent],arr[i]=arr[i],arr[parent]  #否则交换父子节点
            parent=i    #将子节点作为父节点
            i*=2        #交换值后,判断子节点的值是否为子子节点中的最大
    def heapsort(self,arr):
        length=len(arr)
        for i in range(length//2,-1,-1):#i 为每个非叶子节点
            self.build(arr,i,length)
        for i in range(length-1,1,-1):#传入的最小长度为4
            arr[0],arr[i]=arr[i],arr[0]   #把最大值换到末尾
            self.build(arr,0,i)    #数组的长度减一
        arr[0], arr[1] = arr[1], arr[0]    #传入的长度为1的话会出现死循环,因此咱们传入最小长度为2,
                                            # 最后自己手动交换0,1的位置完成最后的排序

a=HeapSort()
arr=[3,4,5,1,4,6,72,4,5]
print(arr)
a.heapsort(arr)
print(arr)
