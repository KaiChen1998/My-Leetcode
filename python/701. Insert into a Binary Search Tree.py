class Solution:
    """
    Problems: 插入一个元素到一棵二叉搜索树当中

    Solutions: 找到他的位置，然后新建结点
    """
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        if(root.val > val):
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val) 
        return root