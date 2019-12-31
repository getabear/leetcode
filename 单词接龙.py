from typing import List
from collections import defaultdict

class Solution1:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #提交后出现超时问题,所以接下来咱们解决子问题
        def judge(src,dest):
            s=len(src)
            d=len(dest)
            si=0
            di=0
            tp=0
            while si<s and di<d:
                if src[si]!=dest[di]:
                    tp+=1
                    if tp>=2:
                        break
                si+=1
                di+=1
            return tp==1
        self.res=float("inf")
        def fun(beginWord: str, endWord: str, wordList: List[str],n):
            if beginWord==endWord:
                if self.res>n:
                    self.res=n
                return
            for i in range(len(wordList)):
                if judge(beginWord,wordList[i]):
                    tp=wordList[:]
                    tp.remove(wordList[i])
                    fun(wordList[i],endWord,tp,n+1)
            return
        if endWord in wordList:
            fun(beginWord,endWord,wordList,1)
        return self.res if self.res!=float("inf") else 0

#单方向广度优先搜索,时间复杂度O(M×N),空间复杂度O(M×N)  M是单词长度,N是单词表中的单词数
class Solution2:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        L=len(beginWord)
        all_combo_dict=defaultdict(list)
        for word in wordList:   #构建邻接表
            for i in range(L):
                #构建只有一个字母不同的单词列表的字典
                all_combo_dict[word[0:i]+"*"+word[i+1:]].append(word)
        #下面利用广度优先搜索
        queue=[(beginWord,1)]
        visited={beginWord:True}
        while queue:
            current_word,level=queue.pop(0)
            for i in range(L):   #遍历所有相差一个字母的节点列表
                intermediate_word=current_word[:i]+"*"+current_word[i+1:]
                for word in all_combo_dict[intermediate_word]:  #遍历所有可以跳转的节点(单词)
                    if word==endWord:   #转移到了endword
                        return level+1
                    if word not in visited:  #如果未被访问过,则加入队列,并标记为访问
                        visited[word]=True
                        queue.append((word,level+1))
        return 0

#方法三:广度优先搜索地双向遍历,更短的时间
class Solution:
    def __init__(self):
        self.L=0
        self.all_combo_dict=defaultdict(list)
    def visitWordNode(self,queue,visited,other_visited):  #函数功能:遍历队列里的第一个节点的周围的所有未遍历过的节点
        current_word,level=queue.pop(0)
        for i in range(self.L):
            intermediate_word=current_word[0:i]+"*"+current_word[i+1:]   #获取只有一个字母不同的字典的键值
            for word in self.all_combo_dict[intermediate_word]:   #遍历这个键值的所有值
                if word in other_visited:
                    return level+other_visited[word]
                if word not in visited:
                    visited[word]=level+1
                    queue.append((word,level+1))
        return None

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        self.L=len(beginWord)
        for word in wordList:      #构建一个只有一个字母不同的字典的值(构建邻接表)
            for i in range(self.L):
                self.all_combo_dict[word[0:i]+"*"+word[i+1:]].append(word)

        visited={beginWord:1}
        other_visited={endWord:1}
        queue=[(beginWord,1)]
        other_queue=[(endWord,1)]
        while queue and other_queue:  #当两个队列都不为空时,开始遍历
            ans=self.visitWordNode(queue,visited,other_visited)
            if ans:
                return ans
            ans=self.visitWordNode(other_queue,other_visited,visited)
            if ans:
                return ans
        return 0




a=Solution()
# beginWord="hot"
# endWord="dog"
# wordList=["hot","cog","dog","tot","hog","hop","pot","dot"]
beginWord="qa"
endWord="sq"
wordList=["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
print(a.ladderLength(beginWord,endWord,wordList))
import time
print(time.process_time())