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


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        L=len(beginWord)
        all_combo_dict=defaultdict(list)
        for word in wordList:
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




a=Solution1()
# beginWord="hot"
# endWord="dog"
# wordList=["hot","cog","dog","tot","hog","hop","pot","dot"]
beginWord="qa"
endWord="sq"
wordList=["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
print(a.ladderLength(beginWord,endWord,wordList))
import time
print(time.process_time())