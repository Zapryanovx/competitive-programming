# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        dq = deque([root])

        level = 1
        max_sum_so_far = root.val
        level_of_max_sum = 1

        while len(dq) > 0:
            curr_sum = 0
            for _ in range(len(dq)):
                curr_node = dq.popleft()
                curr_sum += curr_node.val

                if curr_node.left is not None:
                    dq.append(curr_node.left)
                if curr_node.right is not None:
                    dq.append(curr_node.right)

            if curr_sum > max_sum_so_far:
                max_sum_so_far = curr_sum
                level_of_max_sum = level
            level += 1

        return level_of_max_sum