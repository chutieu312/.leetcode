#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#
# https://leetcode.com/problems/design-twitter/description/
#
# algorithms
# Medium (43.37%)
# Likes:    4796
# Dislikes: 671
# Total Accepted:    373.9K
# Total Submissions: 823.4K
# Testcase Example:  '["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]\n' +
  '[[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]'
#
# Design a simplified version of Twitter where users can post tweets,
# follow/unfollow another user, and is able to see the 10 most recent tweets in
# the user's news feed.
# 
# Implement the Twitter class:
# 
# 
# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId
# by the user userId. Each call to this function will be made with a unique
# tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs
# in the user's news feed. Each item in the news feed must be posted by users
# who the user followed or by the user themself. Tweets must be ordered from
# most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId
# started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId
# started unfollowing the user with ID followeeId.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed",
# "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output
# [null, null, [5], null, null, [6, 5], null, [5]]
# 
# Explanation
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1
# tweet id -> [5]. return [5]
# twitter.follow(1, 2);    // User 1 follows user 2.
# twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2
# tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is
# posted after tweet id 5.
# twitter.unfollow(1, 2);  // User 1 unfollows user 2.
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1
# tweet id -> [5], since user 1 is no longer following user 2.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= userId, followerId, followeeId <= 500
# 0 <= tweetId <= 10^4
# All the tweets have unique IDs.
# At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and
# unfollow.
# A user cannot follow himself.
# 
# 
#

# @lc code=start
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
      self.tweets = defaultdict(list) # userId -> list of (time, tweetId), ex 1 -> [(0, 5), (1, 6)]
      self.following = defaultdict(set) # userId -> set of followeeIds, ex 1 -> {2, 3}
      self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
      self.tweets[userId].append((self.time, tweetId)) # latest tweet is at the end of the list
      self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
      
      userIds = self.following[userId] | {userId}
      heap = []
      
      for uId in userIds:
        if self.tweets[uId]:
          index = len(self.tweets[uId]) - 1 # get the index of the latest tweet will use it lter on
          t, tweetId = self.tweets[uId][index]
          heap.append((-t, tweetId, uId, index)) # use negative time to make it a max heap
          
      heapq.heapify(heap)
      
      ten_news_feed = []
      
      while heap and len(ten_news_feed) < 10:
        _, tweetId, uId, index = heapq.heappop(heap)
        ten_news_feed.append(tweetId)
        index -= 1
        if index >= 0:
          t, tweetId = self.tweets[uId][index] # get the next latest tweet
          heapq.heappush(heap, (-t, tweetId, uId, index))
      
        
      return ten_news_feed

        

    def follow(self, followerId: int, followeeId: int) -> None:
      self.following[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
      self.following[followerId].discard(followeeId)
        
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

