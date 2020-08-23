class Solution:
    """
    Problems:
        Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
        According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

    Solutions 1:
        暴力求解，基于的intuition是最近的公共父节点应该满足：其是共同父节点且子节点都不是共同父节点
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.result = None
        self.dfs(root, p, q)
        return self.result
        
    def dfs(self, root, p, q):
        if(root is None):
            return False
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        if(left or right):
            return True
        else:
            my = self.is_common_ancestor(root, p, q)
            if(my):
                self.result = root
            return my
            
    def is_common_ancestor(self, root, p, q):
        return self.is_ancestor(root, p) and self.is_ancestor(root, q)

    def is_ancestor(self, root, p):
        if(root is None):
            return False
        if(root == p):
            return True
        return self.is_ancestor(root.left, p) or self.is_ancestor(root.right, p)

    """
    Solutions 2:
    如果答案是其中一个节点，不需要搜索另一个结点
    否则，只需要左右节点都有返回就好，因为两个节点一定存在于最近父节点的左右两个分支上
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root is None or root == p or root == q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if (left and right):
            return root
        elif(left is not None):
            return left
        else:
            return right