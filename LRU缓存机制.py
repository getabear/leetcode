class ListNode:
    #一个双向链表结构
    def __init__(self,key=None,value=None):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        #hashmap里的值   {key : ListNode}
        self.hashmap={}

        #head的next属性指向最近使用的键
        self.head=ListNode()

        #tail的prev属性指向最不常用的键
        self.tail=ListNode()

        #初始化头尾节点,并把它们相连接
        self.head.next=self.tail
        self.tail.prev=self.head

    def remove(self,node):
        #函数功能,从双向链表中删除节点node
        node.next.prev=node.prev
        node.prev.next=node.next

    def addNode(self,key,value):
        #函数功能,添加新节点到头部
        x=ListNode(key,value)
        x.next=self.head.next
        x.prev=self.head
        self.head.next.prev=x
        self.head.next=x
        return x

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.remove(self.hashmap[key])#删除原来的节点
            newNode=self.addNode(key,self.hashmap[key].value)#将其移动到头部
            self.hashmap[key]=newNode
            return self.hashmap[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])#删除原来的节点
            newNode=self.addNode(key,value)   #添加一个新节点到双向链表的头部
            self.hashmap[key]=newNode  #更新hashpmap的值
        else:
            #如果容量满了,删除最后一个节点
            if self.capacity==len(self.hashmap):
                self.hashmap.pop(self.tail.prev.key)  #删除hashmap中的键值对
                self.remove(self.tail.prev)  #删除链表中的最后一个节点
            newNode=self.addNode(key,value)  #添加新节点到头部
            self.hashmap[key]=newNode   #添加新的键值对



#很nice,结合了hash表的优点和双向链表的优点,hash表查找块,双向链表有序
#通过了leetcode所有的测试用例击败49%,虽然不高,但是我还是比较满意的

