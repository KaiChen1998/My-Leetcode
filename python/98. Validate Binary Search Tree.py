class Solution:
    """
    Problems: 验证二叉搜索树

    Solutions: 二叉搜索树的中序遍历是升序序列，判断升序成立即可
    """
    def __init__(self):
        self.last = float('-inf')
    def isValidBST(self, root: TreeNode) -> bool:
        # 中序遍历为升序
        if(root is None):
            return True
        if(self.isValidBST(root.left)):
            if(root.val > self.last):
                self.last = root.val
                return self.isValidBST(root.right)
        return False