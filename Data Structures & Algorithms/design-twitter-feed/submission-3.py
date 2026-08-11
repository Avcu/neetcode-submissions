import time
from heapq import heappush, heappop
from collections import deque
class Twitter:

    def __init__(self):
        self.followerDict = dict()
        self.tweetDict = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweetDict:
            self.tweetDict[userId].append([tweetId, time.time()])
        else:
            self.tweetDict[userId] = [[tweetId, time.time()]]

    def getNewsFeed(self, userId: int) -> List[int]:
        relUsers = [userId]
        relTweetsHeap = []
        res = deque()

        # find the relevant users
        if userId in self.followerDict:
            relUsers.extend(self.followerDict[userId])

        # find the relevant tweets
        for relUser in relUsers:
            if relUser in self.tweetDict:
                for tweet in self.tweetDict[relUser]:
                    currTime = tweet[1]
                    currTweetId = tweet[0]
                    heappush(relTweetsHeap, [currTime, currTweetId])

                    if len(relTweetsHeap) > 10:
                        heappop(relTweetsHeap)

        for i in range(len(relTweetsHeap)):
            res.appendleft(heappop(relTweetsHeap)[1])
        return list(res)
            

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return None
        if followerId in self.followerDict:
            if followeeId not in self.followerDict[followerId]:
                self.followerDict[followerId].append(followeeId)
        else:
            self.followerDict[followerId] = [followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followerDict:
            if followeeId in self.followerDict[followerId]:
                self.followerDict[followerId].remove(followeeId)
