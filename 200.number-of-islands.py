#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (62.91%)
# Likes:    25275
# Dislikes: 622
# Total Accepted:    4.4M
# Total Submissions: 6.8M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.
# 
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
# 
# 
# Example 1:
# 
# 
# Input: grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
# 
# 
#

# @lc code=start
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        
        # def dfs(r, c):
        #     if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
        #         return
            
        #     grid[r][c] = '0'
            
        #     dfs(r -1, c)
        #     dfs(r + 1, c)
        #     dfs(r, c - 1)
        #     dfs(r, c + 1)
            
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == '1':
        #             count += 1
        #             dfs(r, c)
                    
        # return count 
        
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = '0'
            
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            
            while q:
                row, col = q.popleft()
            
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    
                    if (r in range(rows) and c in range(cols) and grid[r][c] == '1'):
                        q.append((r, c))
                        grid[r][c] = '0'
                        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    bfs(r, c)
                    
        return count
                
            
  
#   Time: O(rows × columns)    Each cell is visited at most once.  
#   Space: O(rows × columns) cursive DFS stack can contain many cells. The grid itself is reused as the visited map.
        
# @lc code=end

