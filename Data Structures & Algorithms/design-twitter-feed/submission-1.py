import time

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
        res = []
        relUsers = [userId]
        relTweets = []
        res = []

        # find the relevant users
        if userId in self.followerDict:
            relUsers.extend(self.followerDict[userId])

        # find the relevant tweets
        for relUser in relUsers:
            if relUser in self.tweetDict:
                relTweets.extend(self.tweetDict[relUser])
        
        relTweets.sort(key=lambda x: -x[1])

        if len(relTweets) > 10:
            res = [relTweets[x][0] for x in range(10)]
        else:
            res = [x[0] for x in relTweets]
        return res
            

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
