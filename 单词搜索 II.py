from typing import List

class Solution1:
    #第一次提交超时了
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        high=len(board)
        width=len(board[0])

        #访问的记录
        visited=[[0 for i in range(width)] for j in range(high)]
        direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 方向数组

        def fun(visited,x,y,index,word,length):
            if(index==length):
                return True
            for dx,dy in direct:
                if(x+dx<high and y+dy<width and x+dx>=0 and y+dy>=0 and\
                        visited[x+dx][y+dy]==0 and word[index]==board[x+dx][y+dy]):
                    visited[x+dx][y+dy]=1
                    if(fun(visited,x+dx,y+dy,index+1,word,length)):
                        visited[x + dx][y + dy] = 0
                        return True
                    visited[x + dx][y + dy] = 0
            return False

        ret=[]
        flag=0
        for word in words:
            for i in range(high):
                for j in range(width):
                    if(board[i][j]==word[0]):
                        visited[i][j]=1
                        if(fun(visited,i,j,1,word,len(word))):
                            ret.append(word)
                            flag=1
                        visited[i][j]=0
                        if(flag):
                            break
                if(flag):
                    break
            flag=0
        return ret


#使用前缀树,击败92%
class Solution2:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie={}
        high=len(board)
        width=len(board[0])

        for word in words:   #构建前缀树
            node=trie
            for i in word:
                if i not in node:
                    node[i]={}
                node=node[i]
            node["#"]=word  #标志单词结束,等于word是因为方便最后添加到返回值中(其实什么都可以等于,例如"#")

        direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]  #方向数组
        ret=[]
        def fun(x,y,tmp):   #参数说明:x,y为坐标   tmp为前缀树
            current=board[x][y]    #当前字母
            curNode=tmp[current]
            if("#" in curNode):
                ret.append(curNode["#"])   #找到一个单词
            board[x][y]="."   #标记已经访问过的字母
            for dx,dy in direct:
                if(x+dx<0 or x+dx>=high or y+dy<0 or y+dy>=width):
                    continue     #超出范围,则不管
                if board[x+dx][y+dy] not in curNode:
                    continue
                fun(x+dx,y+dy,curNode)
            board[x][y] =current

        for i in range(high):
            for j in range(width):
                curNode=trie
                if(board[i][j] in curNode):
                    fun(i,j,curNode)

        return ret

#官方   击败97% 真厉害
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'

        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word

        rowNum = len(board)
        colNum = len(board[0])

        matchedWords = []

        def backtracking(row, col, parent):

            letter = board[row][col]
            currNode = parent[letter]

            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)

            # Before the EXPLORATION, mark the cell as visited
            board[row][col] = '#'

            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)

            # End of EXPLORATION, we restore the cell
            board[row][col] = letter

            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:   # 剪枝,所以速度更加的快
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matchedWords




a=Solution()
words = ["oath","pea","eat","rain"]
board =[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
print(a.findWords(board,words))