from  collections import defaultdict

class Node:
    def __init__(self,key,val,pre=None,next=None,freq=0):
        self.pre=pre
        self.next=next
        self.freq=freq
        self.val=val
        self.key=key

    def insert(self,node):   #插入node节点到self后
        node.next=self.next
        node.pre=self
        self.next.pre=node
        self.next=node

def creat_linked_list():
    head=Node(0,0)
    tail=Node(0,0)
    tail.pre=head
    head.next=tail
    return (head,tail)


class LFUCache:

    def __init__(self, capacity: int):
        self.maxCount=capacity
        self.freqMap=defaultdict(creat_linked_list)
        self.keyMap={}
        self.minFreq=0
        self.size=0

    def delete(self,node):
        if node.pre:
            node.pre.next=node.next
            node.next.pre=node.pre
            # ferqMap的值只包含首节点和尾节点,即默认的creat_linked_list
            if node.pre is self.freqMap[node.freq][0] and node.next is self.freqMap[node.freq][1]:
                self.freqMap.pop(node.freq)
        return node.key

    def increase(self,node):
        node.freq+=1
        self.delete(node)
        self.freqMap[node.freq][1].pre.insert(node)
        if node.freq==1:
            self.minFreq=node.freq
        elif node.freq-1==self.minFreq:
            head,tail=self.freqMap[node.freq-1]
            if head.next is tail:
                self.minFreq=node.freq

    def get(self, key: int) -> int:
        if key in self.keyMap:
            node=self.keyMap[key]
            self.increase(node)
            return node.val
        return -1
    def put(self, key: int, value: int) -> None:
        if self.maxCount!=0:
            if key in self.keyMap:
                node=self.keyMap[key]
                node.val=value
            else:
                node=Node(key,value)
                self.keyMap[key]=node
                self.size+=1
            if self.size>self.maxCount:
                self.size-=1
                deleted=self.delete(self.freqMap[self.minFreq][0].next)
                self.keyMap.pop(deleted)
            self.increase(node)


