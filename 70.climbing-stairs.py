# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
# Difficulty: Easy
# Topic: Dynamic Programming (Fibonacci pattern)
#
# Problem:
#   You can climb 1 or 2 steps at a time.
#   How many distinct ways can you climb to the top of an n-step staircase?
#
# Examples:
#   n=2 → 2  (1+1, 2)
#   n=3 → 3  (1+1+1, 1+2, 2+1)
#
# Key insight: ways(n) = ways(n-1) + ways(n-2)  — it IS Fibonacci.
#   ways(n-1): we were one step below, took 1 step.
#   ways(n-2): we were two steps below, took 2 steps.
#
# Approach: Space-optimised DP — only keep the last two values.
# Time:  O(n)
# Space: O(1)


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev2, prev1 = 1, 2          # ways(1), ways(2)
        for _ in range(3, n + 1):
            prev2, prev1 = prev1, prev2 + prev1
        return prev1


# ---------------------------------------------------------------------------
# Interview talking point
# ---------------------------------------------------------------------------
# "This reduces to Fibonacci. At each step k, the number of ways equals
#  ways(k-1) + ways(k-2) because those are the only two positions we could
#  have been standing on just before arriving at k.
#  I use two variables instead of an array to keep space O(1).
#  Base cases: n=1 → 1 way, n=2 → 2 ways, then iterate up to n."
#
# Brute-force comparison (O(2^n) — mention to show you know the trade-off):
#   def climbStairs(self, n):
#       if n <= 1: return 1
#       return self.climbStairs(n-1) + self.climbStairs(n-2)
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(1))   # 1
    print(s.climbStairs(2))   # 2
    print(s.climbStairs(3))   # 3
    print(s.climbStairs(5))   # 8
    print(s.climbStairs(10))  # 89
