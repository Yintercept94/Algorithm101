# 94. 二叉树的中序遍历
# Easy
# Topics: Tree
#
# https://leetcode.cn/problems/binary-tree-inorder-traversal/description/
#
# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

 

# 示例 1：


# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
# 示例 2：

# 输入：root = []
# 输出：[]
# 示例 3：

# 输入：root = [1]
# 输出：[1]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lst=[]
        def dfs(t):
            if not t:
                return
            dfs(t.left)
            lst.append(t.val)
            dfs(t.right)
        dfs(root)
        return lst
        
 
