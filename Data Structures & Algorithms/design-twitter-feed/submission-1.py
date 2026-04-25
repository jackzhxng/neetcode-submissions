from collections import defaultdict, deque
from datetime import datetime
from typing import Dict, List
from itertools import islice
import heapq

class Tweet:
    def __init__(self, id: int, user_id: int):
        self.id = id
        self.user_id = user_id
        self.created_at = datetime.now()

class Twitter:
    """
    Time: 45 mins

    This solution favors fan out on push over fan in on pull (which is a lot easier to implement).
    LC will favor the latter since there doesn't seem to be a lot more getNewsFeed calls relative to the
    others but this is just here for practice.
    """
    def __init__(self):
        self.tweets: Dict[int, deque[Tweet]] = defaultdict(deque) # Maps user id to deque of tweets
        self.follows: Dict[int, set[int]] = defaultdict(set) # Maps user id to set of user ids - who the user follows
        self.followers: Dict[int, set[int]] = defaultdict(set) # Maps user id to set of user ids - who follows the user
        self.newsfeeds: Dict[int, deque[Tweet]] = defaultdict(deque) # Maps user id to deque of tweets - represents a cache of each user's newsfeed

    def _merge_first_ten_tweets(self, a: deque[Tweet], b: deque[Tweet]) -> deque[Tweet]:
        a_i, b_i = 0, 0
        res = deque()
        while a_i < len(a) and b_i < len(b) and len(res) < 10:
            tweet_a = a[a_i]
            tweet_b = b[b_i]
            if tweet_a.created_at > tweet_b.created_at:
                res.append(tweet_a)
                a_i += 1
            else:
                res.append(tweet_b)
                b_i += 1
        while a_i < len(a) and len(res) < 10:
            tweet_a = a[a_i]
            res.append(tweet_a)
            a_i += 1
        while b_i < len(b) and len(res) < 10:
            tweet_b = b[b_i]
            res.append(tweet_b)
            b_i += 1
        assert len(res) <= 10
        return res

    def postTweet(self, userId: int, tweetId: int) -> None:
        """O(n), n is number of users"""
        new_tweet = Tweet(tweetId, userId)
        self.tweets[userId].appendleft(new_tweet)
        if len(self.tweets[userId]) > 10:
            _ = self.tweets[userId].pop()

        # Broadcast to the newsfeeds of rest of the followers and user himself
        for followerId in self.followers[userId] | {userId}:
            self.newsfeeds[followerId].appendleft(new_tweet)
            if len(self.newsfeeds[followerId]) > 10:
                _ = self.newsfeeds[followerId].pop()

    def getNewsFeed(self, userId: int) -> List[int]:
        """O(1) - Assuming that this will be the most frequent call based how people use Twitter"""
        return [tweet.id for tweet in self.newsfeeds[userId]]

    def follow(self, followerId: int, followeeId: int) -> None:
        """"O(1) - just performing 10 comparisons among 2 sorted lists"""
        if followerId == followeeId:
            return
        if followeeId in self.follows[followerId]:
            return
        self.follows[followerId].add(followeeId)
        self.followers[followeeId].add(followerId)

        # Update follower's newsfeed
        # Merge follower's current news feed with followee's tweets up to len 10
        updated_newsfeed = self._merge_first_ten_tweets(
            self.newsfeeds[followerId],
            self.tweets[followeeId],
        )
        self.newsfeeds[followerId] = updated_newsfeed

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """O(log n) - where n is number of followees, technically O(10*log n) since you pop off the heap 10 times, but 10 is constant."""
        if followerId == followeeId:
            return
        if followeeId not in self.follows[followerId]:
            return
        self.follows[followerId].discard(followeeId)
        self.followers[followeeId].discard(followerId)

        # Update follower's newfeed
        candidates = [self.tweets[followeeId] for followeeId in self.follows[followerId]] + [self.tweets[followerId]]
        new_newsfeed = heapq.merge(*candidates, key=lambda tweet : tweet.created_at, reverse=True)
        self.newsfeeds[followerId] = deque(islice(new_newsfeed, 10))

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)