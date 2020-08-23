class Solution:
    """
    Problems:
        Given a non-empty binary tree, find the maximum path sum.
        For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

    Solutions:
        任意一条最大路径，其根节点（深度最低的点）的情况只可能有两种，一种是作为整棵树的根节点向左右都有延伸，另一种是作为这条路径的一个端点
        但是DFS过程中我们总是记录第二种情况，即返回的结果都是以该结点为端点，向其中一边
        最终的结果用另外的变量缓存
    """
    def maxPathSum(self, root: TreeNode) -> int:
        self.result = float('-inf')
        self.dfs(root)
        return self.result

    def dfs(self, root):
        # dfs返回的是以当前节点为终点的路径的长度
        if root is None:
            return 0
        # 如果延伸到这个孩子节点的这条最大路径和为负值，肯定直接舍弃
        left = max(0, self.dfs(root.left))
        right = max(0, self.dfs(root.right))
        self.result = max(self.result, left + right + root.val)
        return max(left, right) + root.val
