
class BigHeap:
    def __init__(self,k):
        # 堆中剩余的数是最小的K个数
        MaxNum=(1<<31)   #自己假定的最大值
        self.heap=[MaxNum for _ in range(k+1)]
        self.length=k
    def build_heap(self,child):
        while(child>1):
            parent=child//2
            if child & 0x1:   #保证child是左节点
                child -= 1
            left=child
            if left+1 < self.length and self.heap[left] < self.heap[left+1]:
                left = left+1
            if self.heap[parent] < self.heap[left]:
                self.heap[parent],self.heap[left]=self.heap[left],self.heap[parent]
                self.heap_down(left,self.length)
            child = parent
        return
    def heap_down(self,parent,length):    #负责某个节点的下沉
        # parent为要下沉的节点的下标
        while parent<=length//2:
            LeftChild=2*parent
            RightChild=LeftChild+1
            # 找出子节点较大的节点
            if RightChild <= length and self.heap[LeftChild]<self.heap[RightChild]:
                LeftChild=RightChild
            # 如果父节点比子节点小，则需要下沉
            if self.heap[parent]<self.heap[LeftChild]:
                self.heap[parent],self.heap[LeftChild]=self.heap[LeftChild],self.heap[parent]
                parent=LeftChild
            else:
                break
        return
    def insert(self,num):
        if num < self.heap[1]:  #如果小于堆顶的数，将其加入
            self.heap[1]=num
            self.heap_down(1,self.length)
        return
    def heap_sort(self):
        k=self.length
        while k > 1:
            self.heap[k],self.heap[1]=self.heap[1],self.heap[k]
            k -= 1
            self.heap_down(1,k)

        return self.heap
# 测试
nums=[100,88,1,3,20,100,70,23,1,412,432,123,54,231,4532]
a=BigHeap(len(nums))
for i in nums:
    a.insert(i)
a.heap_sort()
print(a.heap[1:])
nums.sort()
print(nums)