class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#这里写复杂了,我妄图直接找到第一个不重复的节点,赋值给tp(即前项指针),这里
#更简单的方法是新建一个虚拟节点例如 tp=ListNode(-1) ret=tp 返回时返回ret.next
#感叹大佬们的智慧
class Solution:
    #自己写的,细节处理太多了,头很痛,而且只击败了19%的用户
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        sp = head
        if head.next != None:
            fp = head.next
        else:
            return head
        tp = None  # 用以记录sp的前项指针

        # 找第一个有效节点,并用tp指向它
        if sp.val == fp.val:  # 如果相等了,说明有重复
            while (1):
                while fp and fp.val == sp.val:
                    fp = fp.next
                sp = fp
                if fp == None or (fp.next and fp.val != fp.next.val) or fp.next == None:
                    tp = fp  # 记录第一个不重复的节点的值
                    if fp != None:
                        fp = fp.next
                    else:
                        return None
                    break
                if fp != None:
                    fp = fp.next
                else:
                    return None
        else:
            tp = sp
        ret = tp  # 记录返回头结点

        while (fp):
            if sp.val == fp.val:  # 发现一样了,sp需要回退
                while fp and fp.val == sp.val:
                    fp = fp.next
                sp = tp  # 回退
                sp.next = fp
                sp = fp
            else:
                tp = sp
                sp = fp
            if fp != None:
                fp = fp.next
            else:
                break
        return ret

#递归版本,大佬写的,我没想过
class Solution1:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:return head
        if head.next and head.val == head.next.val:   #如果相等,移动到下一个不相等的节点
            while head.next != None and head.val == head.next.val:#移动到下一个不相等的节点
                head = head.next
            return self.deleteDuplicates(head.next)
        else:#否则,该节点是有效的,只有一个值的节点,并把其next指针指向下一个有效节点
            head.next = self.deleteDuplicates(head.next)
        return head   #返回有效节点


