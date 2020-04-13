from typing import List

class Twitter:

    class Node:
        def __init__(self):
            self.follow=set()   #记录自己的关注
            self.tweet=[]    #记录自己的文章和文章发表的时间

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time=0   #记录每个tweet的时间
        self.users={}  #记录所有用户


    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.users:
            self.users[userId]=Twitter.Node()
        self.users[userId].tweet.append((tweetId,self.time))
        self.time+=1


    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.users:
            return []
        ret=self.users[userId].tweet[-10:][::-1] #取列表最后10个数据,并且将其翻转
        for tmp in self.users[userId].follow:
            ans=[]
            if tmp in self.users:
                ans=self.users[tmp].tweet[-10:][::-1]
            i,j=0,0
            combined=[]
            while i<len(ret) and j<len(ans):
                if ret[i][1]>ans[j][1]:  #如果后发
                    combined.append(ret[i])
                    i+=1
                else:
                    combined.append(ans[j])
                    j+=1
            combined.extend(ret[i:])
            combined.extend(ans[j:])
            ret=combined[:10]

        opt=[]
        for i in ret:
            opt.append(i[0])

        return opt

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.users:
            self.users[followerId]=Twitter.Node()
        if followerId!=followeeId:
            self.users[followerId].follow.add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId!=followeeId:
            if followerId in self.users:
                # 该方法不同于 remove() 方法，因为remove()方法在移除一个不存在的元素时会
                # 发生错误，discard() 方法不会。
                self.users[followerId].follow.discard(followeeId)


a=Twitter()
a.follow(1,5)
print(a.getNewsFeed(1))

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)