from typing import List
from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        #思路,我先使用广度优先搜索算出最短的距离,然后使用深度优先遍历去寻找记录路径,算法是正确的不过最后超时了
        #时间复杂度过高,看能不能优化
        self.min_step=0
        self.ret=[]
        self.dict=defaultdict(list)
        # 首先建立邻接表
        length=len(wordList)   #单词表的长度
        if length==0:
            return []
        length=len(wordList[0])   #每个单词的长度
        dic=defaultdict(list)
        for word in wordList:   #构建邻接表
            for i in range(length):
                dic[word[:i]+'*'+word[i+1:]].append(word)

        def bfs(dic):    #函数用于寻找最短路径
            queue=[(beginWord,1)]    #广度优先搜索用的队列
            temp=[beginWord]
            visited={beginWord:True}  #标记是否访问过该节点
            flag=False
            while(queue):
                cur,step=queue.pop(0)
                for i in range(length):
                    tp=cur[:i]+'*'+cur[i+1:]
                    for word in dic[tp]:
                        if word==endWord:
                            self.min_step=step+1
                            temp.append(word)
                            flag=True
                        elif word not in visited:
                            visited[word]=True
                            queue.append((word,step+1))
                            temp.append(word)
                if flag:
                    break
            for word in temp:  # 构建邻接表
                for i in range(length):
                    self.dict[word[:i] + '*' + word[i + 1:]].append(word)
            return 0

        if endWord not in wordList or not wordList or not beginWord or not endWord:
            return []
        bfs(dic)
        if self.min_step == 0 :  #没找到从beginword到endword的路径
            return []
        def find(word,step,visited,steps):
            if word==endWord:
                if steps not in self.ret:
                    self.ret.append(steps[:])
                return
            if step>=self.min_step:
                return
            for i in range(length):
                tp=word[:i]+"*"+word[i+1:]
                for tp2 in self.dict[tp]:
                    if tp2 not in visited:
                        visited[tp2]=True
                        find(tp2,step+1,visited,steps+[tp2])
                        visited.pop(tp2)
            return
        find(beginWord,1,{beginWord:True},[beginWord])
        return self.ret







#
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
beginWord="a"
endWord="c"
wordList=["a","b","c"]
a=Solution()
print(a.findLadders(beginWord,endWord,wordList))


class Solution1:
     # 我被恶心到了,大佬的代码和我的代码不同之处在于,大佬的代码记录了每个单词到begword的最小距离,如果不是,就不dfs搜索
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        from collections import defaultdict
        wordList = set(wordList)
        res = []
        # 记录单词下一步能转到的单词
        next_word_dict = defaultdict(list)
        # 记录到beginWord距离
        distance = {}
        distance[beginWord] = 0

        # 找一个单词能转到的单词
        def next_word(word):
            ans = []
            for i in range(len(word)):
                for j in range(97, 123):
                    tmp = word[:i] + chr(j) + word[i + 1:]
                    if tmp != word and tmp in wordList:
                        ans.append(tmp)
            return ans

        # 求到beginWord的距离
        def bfs():
            cur = [beginWord]
            step = 0
            flag = False
            while cur:
                step += 1
                next_time = []
                for word in cur:
                    for nw in next_word(word):
                        next_word_dict[word].append(nw)
                        if nw == endWord:
                            flag = True
                        if nw not in distance:
                            distance[nw] = step
                            next_time.append(nw)
                if flag:
                    break
                cur = next_time
            # 遍历所有从beginWord到endWord的路径

        def dfs(tmp, step):
            if tmp[-1] == endWord:
                res.append(tmp)
                return
            for word in next_word_dict[tmp[-1]]:
                if distance[word] == step + 1:
                    dfs(tmp + [word], step + 1)

        bfs()
        dfs([beginWord], 0)
        return res


