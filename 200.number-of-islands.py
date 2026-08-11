# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/
# Difficulty: Medium
# Topic: Graphs / DFS / BFS
#
# Problem:
#   Given an m×n grid of '1' (land) and '0' (water), count the number of islands.
#   An island is surrounded by water and formed by connecting adjacent lands
#   horizontally or vertically.
#
# Example:
#   grid = [
#     ["1","1","0","0","0"],
#     ["1","1","0","0","0"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"],
#   ]
#   Output: 3
#
# Approach: DFS flood-fill.
#   Scan every cell. When we hit an unvisited '1', increment count and DFS to
#   mark the entire connected island as visited (sink it to '0' in-place).
#
# Time:  O(m × n)
# Space: O(m × n) worst-case recursion stack (all land)

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # Out of bounds or water — stop
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return
            grid[r][c] = "0"          # mark visited by sinking the cell
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)         # sink the whole island
        return count


# ---------------------------------------------------------------------------
# Interview talking point
# ---------------------------------------------------------------------------
# "I treat the grid as a graph where adjacent '1' cells are connected edges.
#  I scan every cell; when I find unvisited land I know it's a new island so
#  I increment the counter and DFS to sink every connected cell to '0' —
#  marking them visited without a separate boolean matrix.
#  O(m×n) time since each cell is visited at most once."
#
# BFS alternative (avoids recursion depth issues on huge grids):
#   Use a deque, push the seed cell, then BFS all 4 neighbours.
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    s = Solution()
    g1 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(s.numIslands(g1))  # 3

    g2 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    print(s.numIslands(g2))  # 1
