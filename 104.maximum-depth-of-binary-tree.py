# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Difficulty: Easy
# Topic: Trees / DFS / BFS
#
# Problem:
#   Given the root of a binary tree, return its maximum depth (number of nodes
#   along the longest root-to-leaf path).
#
# Example:
#       3
#      / \
#     9  20
#        / \
#       15   7
#   Output: 3
#
# Approach A (recursive DFS): depth = 1 + max(left_depth, right_depth)
# Approach B (iterative BFS): count levels while queue is non-empty.
# Time:  O(n)
# Space: O(h) — h = tree height (O(log n) balanced, O(n) worst-case)

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # --- Approach A: recursive DFS (most concise) ---
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # --- Approach B: iterative BFS (good to mention in interviews) ---
    def maxDepth_bfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)):   # process one full level at a time
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth


# ---------------------------------------------------------------------------
# Interview talking point
# ---------------------------------------------------------------------------
# "The recursive solution reads almost like the definition: the depth of an
#  empty tree is 0; otherwise it's 1 (current node) plus the deeper of the
#  two subtrees. I can also do it iteratively with BFS — I count how many
#  levels I dequeue before the queue empties. Both are O(n) time.
#  I default to recursive for clarity, but BFS avoids stack-overflow risk
#  on very deep trees."
# ---------------------------------------------------------------------------


# Quick smoke test
if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    s = Solution()
    print(s.maxDepth(root))      # 3
    print(s.maxDepth_bfs(root))  # 3
    print(s.maxDepth(None))      # 0
