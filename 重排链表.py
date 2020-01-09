from git import lian

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    #毫无悬念的超时啦,因为每次都需要去找末尾节点,很耗时间
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #本来无思路,在草稿本上写了下,知道怎么写了,哈哈哈哈,果然有时候写下思路就出来了
        def fun(head: ListNode,pre):   #函数功能返回末尾节点

            # 到达末尾节点
            if not head.next:
                # 将前一个节点置为末尾
                pre.next=None
                return head

            return fun(head.next,head)
        ret=head
        while head:
            tp=head.next
            if head.next and tp.next:   #如果不是末尾节点
                res=fun(head.next,head)
                head.next=res
                res.next=tp
            head=tp

        return ret

class Solution:
    #提交后击败84%的用户   时间复杂度O(n)
    def reorderList(self, head: ListNode) -> None:
        ret=head
        stack=[]
        while head:     #一次遍历构建一个链表的栈,方便查找最后一个节点
            stack.append(head)
            head=head.next
        head=ret
        while head:
            tp=head.next
            last=stack.pop()
            if tp==last or head==last:
                break
            head.next=last
            last.next=tp
            head=tp
        if ret:   #如果head为空就不会有last变量
            last.next=None
        return ret


b=lian()
head=b.creat([1,2,3,4,5])
a=Solution()
head=a.reorderList(head)
print("end")









