
# Trie 树优于哈希表的另一个理由是，随着哈希表大小增加，会出现大量的冲突，时间复杂度可能增加到 O(n)
# 其中 nn 是插入的键的数量。与哈希表相比，Trie 树在存储多个具有相同前缀的键时可以使用较少的空间。
# 此时 Trie 树只需要 O(m) 的时间复杂度，其中 mm 为键长。而在平衡树中查找键值需要 O(mlogn)
# 时间复杂度。

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie={}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree=self.trie
        for i in word:
            if i not in tree:
                tree[i]={}
            tree=tree[i]
        tree["#"]="#"

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree=self.trie
        for i in word:
            if i in tree:
                tree=tree[i]
            else:
                return False
        if("#" in tree):
            return True
        else:
            return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.trie
        for i in prefix:
            if i in tree:
                tree = tree[i]
            else:
                return False
        return True
