class Solution:
    """
    Problem:
        Given a binary tree, determine if it is height-balanced.
        For this problem, a height-balanced binary tree is defined as:
            a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

    Solutions:
        重点在于如果有一棵子树违反了balance都要将这个结果向上传递，不能简单地计算root两棵子树的高度差
    """
    def isBalanced(self, root: TreeNode) -> bool:
        return self.height(root) >= 0

    def height(self, root):
        # value set: [-1, 0, 1]
        if(root is None):
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        if((left >= 0) and (right >= 0) and (abs(left - right) <= 1)):
            return max(left, right) + 1
        else:
            return -1