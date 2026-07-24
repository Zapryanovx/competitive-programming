# https://leetcode.com/problems/path-sum-iii/description

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.cnt = 0
        self.dfs(root, targetSum)
        return self.cnt

    def dfs(self, root: Optional[TreeNode], targetSum: int):
        if root is None:
            return

        self.dfs2(root, targetSum, 0)
        self.dfs(root.left, targetSum)
        self.dfs(root.right, targetSum)

    def dfs2(self, node: Optional[TreeNode], targetSum: int, currSum: int):
        if node is None:
            return

        if node.val + currSum == targetSum:
            self.cnt += 1
        currSum += node.val

        self.dfs2(node.left, targetSum, currSum)
        self.dfs2(node.right, targetSum, currSum)