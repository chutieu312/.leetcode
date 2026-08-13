#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (53.68%)
# Likes:    24779
# Dislikes: 1054
# Total Accepted:    5.4M
# Total Submissions: 10M
# Testcase Example:  '2'
#
# You are climbing a staircase. It takes n steps to reach the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# 
# Example 1:
# 
# 
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# 
# 
# Example 2:
# 
# 
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 45
# 
# 
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        for step in range(3, n + 1):
            dp[step] = dp[step - 1] + dp[step - 2]
            
        return dp[n]
    
        # two_steps_before = 1
        # one_step_before = 2

        # for step in range(3, n + 1):
        #     current = two_steps_before + one_step_before
        #     two_steps_before = one_step_before
        #     one_step_before = current

        # return one_step_before
    
        
    # Complexity:
    # Time: O(n), because the loop calculates dp[3] through dp[n], and each step
    # takes constant time by adding two values that are already stored.
    # Space: O(n), because dp stores one answer for every step from 0 through n.
    #
    # Why this is dynamic programming:
    # dp[step] represents the number of ways to reach this step. To reach step,
    # the last move must come from either step - 1 or step - 2, so the recurrence
    # is dp[step] = dp[step - 1] + dp[step - 2]. This problem has overlapping
    # subproblems because the same smaller step counts are needed repeatedly, and
    # it has optimal substructure because each answer is built from smaller answers.
    # To recognize DP here, look for a question asking for the number of ways to
    # reach a state where each move has limited choices and earlier results can be
    # reused to calculate the next result.

# @lc code=end

