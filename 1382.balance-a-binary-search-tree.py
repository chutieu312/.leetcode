#
# @lc app=leetcode id=1382 lang=python3
#
# [1382] Balance a Binary Search Tree
#
# https://leetcode.com/problems/balance-a-binary-search-tree/description/
#
# algorithms
# Medium (84.71%)
# Likes:    4201
# Dislikes: 105
# Total Accepted:    414.3K
# Total Submissions: 480.2K
# Testcase Example:  '[1,null,2,null,3,null,4]'
#
# Given the root of a binary search tree, return a balanced binary search tree
# with the same node values. If there is more than one answer, return any of
# them.
# 
# A binary search tree is balanced if the depth of the two subtrees of every
# node never differs by more than 1.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2] is also
# correct.
# 
# 
# Example 2:
# 
# 
# Input: root = [2,1,3]
# Output: [2,1,3]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# 1 <= Node.val <= 10^5
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
# @lc code=end

