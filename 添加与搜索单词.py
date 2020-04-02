class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words={}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        size=len(word)
        if(size in self.words):
            self.words[size]+=[word]  #字典的键为单词长度,值为一个数组
        else:
            self.words[size]=[word]


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        size=len(word)
        try:
            for i in self.words[size]:
                index=0
                for j in range(size):
                    if i[j]==word[j] or word[j]=='.':
                        index+=1
                    else:
                        break
                if(index==size):
                    return True
        except:
            return False
        return False