import heapq
from collections import defaultdict, deque

# https://leetcode.com/problems/design-twitter/description/

# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user,
# and is able to see the 10 most recent tweets in the user's news feed.

# Implement the Twitter class:

# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId.
# Each call to this function will be made with a unique tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed.
# Each item in the news feed must be posted by users who the user followed or by the user themself.
# Tweets must be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

# Example 1:
# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output
# [null, null, [5], null, null, [6, 5], null, [5]]

# Explanation
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
# twitter.follow(1, 2);    // User 1 follows user 2.
# twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.unfollow(1, 2);  // User 1 unfollows user 2.
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.

# Constraints:
# 1 <= userId, followerId, followeeId <= 500
# 0 <= tweetId <= 104
# All the tweets have unique IDs.
# At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.


class Twitter(object):
    """
    Time -> O(N) or O(10*K) where K are number of followers who tweeted
    Space -> O(N)
    """

    def __init__(self):
        self.time = -1
        self.tweets = defaultdict(deque)
        self.followers = defaultdict(set)

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        # for min-heap purposes
        self.time -= 1
        self.tweets[userId].appendleft((self.time, tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop()

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        feed = []

        # get tweets by followers including user
        for follower in self.followers[userId] | {userId}:
            # if user has tweeted
            if follower in self.tweets and self.tweets[follower]:
                tweets = self.tweets[follower]
                feed.append(tweets)

        news_feed = list(heapq.merge(*(tweets for tweets in feed)))
        return [tweetId for _, tweetId in news_feed[:10]]

        # can also be as follows but above is more verbose and clearer plus takes care of edge case
        # where the follower doesn't have tweets
        # tweets = list(heapq.merge(
        # *(self.tweets[followee] for followee in self.followers[userId] | {userId})))
        # return [tweetId for _, tweetId in tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)


if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 5)  # User 1 posts a new tweet (id = 5).
    twitter.getNewsFeed(
        1
    )  # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
    twitter.follow(1, 2)  # User 1 follows user 2.
    twitter.postTweet(2, 6)  # User 2 posts a new tweet (id = 6).
    twitter.getNewsFeed(
        1
    )  # User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
    twitter.unfollow(1, 2)  # User 1 unfollows user 2.

    # User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
    print(twitter.getNewsFeed(1))
