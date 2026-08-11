import time
from heapq import heappush, heappop

class Twitter:

    def __init__(self):
        self.followerDict = defaultdict(set)
        self.tweetDict = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweetDict:
            self.tweetDict[userId].append([tweetId, time.time()])
        else:
            self.tweetDict[userId] = [[tweetId, time.time()]]

    def getNewsFeed(self, userId: int) -> List[int]:
        relUsers = [userId]
        relTweetsHeap = []
        res = []

        # find the relevant users
        if userId in self.followerDict:
            relUsers.extend(self.followerDict[userId])

        # add the most recent tweet from each user
        for relUser in relUsers:
            if relUser in self.tweetDict:
                currIdx = len(self.tweetDict[relUser]) - 1
                curTime = self.tweetDict[relUser][currIdx][1]
                currTweetId = self.tweetDict[relUser][currIdx][0]
                heappush(relTweetsHeap, [-curTime, currTweetId, relUser, currIdx])

        while relTweetsHeap and len(res) < 10:
            # pop the most recent tweet from the heap
            poppedTweet = heappop(relTweetsHeap)
            res.append(poppedTweet[1])

            # get another tweet from the same user and push it into the heap
            idx = poppedTweet[3] - 1
            user = poppedTweet[2]
            if idx > -1:
                curTime = self.tweetDict[user][idx][1]
                currTweetId = self.tweetDict[user][idx][0]
                heappush(relTweetsHeap, [-curTime, currTweetId, user, idx])
        
        return res
            

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followerDict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followerDict:
            if followeeId in self.followerDict[followerId]:
                self.followerDict[followerId].remove(followeeId)
