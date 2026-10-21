
import heapq
from collections import defaultdict


class Twitter:

    def __init__(self):
        self.time = 0

        # userId -> list of (timestamp, tweetId)
        self.tweets = defaultdict(list)

        # userId -> set of followee IDs
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []

        # Include the user's own tweets and followed users' tweets
        users = self.following[userId] | {userId}

        for uid in users:
            tweets = self.tweets[uid]

            # Add each user's most recent tweet to the heap
            if tweets:
                index = len(tweets) - 1
                timestamp, tweetId = tweets[index]
                heapq.heappush(
                    heap, (-timestamp, tweetId, uid, index)
                )

        feed = []

        # Retrieve up to 10 most recent tweets
        while heap and len(feed) < 10:
            _, tweetId, uid, index = heapq.heappop(heap)
            feed.append(tweetId)

            # Add the next older tweet from the same user
            index -= 1
            if index >= 0:
                timestamp, nextTweetId = self.tweets[uid][index]
                heapq.heappush(
                    heap, (-timestamp, nextTweetId, uid, index)
                )

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

