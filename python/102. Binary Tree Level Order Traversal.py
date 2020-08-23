class Solution:
    """
    Solution 1: 队列实现层序遍历，等于一行一行走
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if(root is not None):
            queue = [root]
            while(len(queue) > 0):
                level_size = len(queue)
                current_size = 0
                level_result = []
                while(current_size < level_size):
                    current_size += 1
                    top = queue.pop(0)
                    level_result.append(top.val)
                    if(top.left is not None):
                        queue.append(top.left)
                    if(top.right is not None):
                        queue.append(top.right)
                result.append(level_result)
        return result

    """
    Solution 2: 先验分布缓存层序分布，等于一列一列走
    """

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if(root is not None):
            self.dfs(root, 0, result)
        return result
    
    def dfs(self, root, depth, result):
        if(root is not None):
            if(len(result) <= depth):
                result.append([root.val])
            else:
                result[depth].append(root.val)
            self.dfs(root.left, depth + 1, result)
            self.dfs(root.right, depth + 1, result)