import time
import random

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Tree:
    def __init__(self, num_list):
        self.root = create_Tree(num_list, 0)

    def height(self, is_recursive = 1):
        if(is_recursive):
            return height_recursive(self.root)
        else:
            return height_norecur(self.root)

    def pre_order(self, is_recursive = 1):
        result = []
        if(is_recursive):
            pre_order_recursive(self.root, result)
        else:
            result = pre_order_norecur(self.root)
        return result
    
    def in_order(self, is_recursive = 1):
        result = []
        if(is_recursive):
            in_order_recursive(self.root, result)
        else:
            result = in_order_norecur(self.root)
        return result
    
    def post_order(self, is_recursive = 1):
        result = []
        if(is_recursive):
            post_order_recursive(self.root, result)
        else:
            result = post_order_norecur(self.root)
        return result

    def level_order(self):
        result = []
        queue = [self.root]
        while(len(queue) > 0):
            top = queue.pop(0)
            result.append(top.val)
            if(top.left is not None):
                queue.append(top.left)
            if(top.right is not None):
                queue.append(top.right)
        return result

def create_Tree(num_list, index):
    if(index >= len(num_list) or num_list[index] == 'null'):
        return None
    root = TreeNode(num_list[index])
    root.left = create_Tree(num_list, 2 * index + 1)
    root.right = create_Tree(num_list, 2 * index + 2)
    return root

##################################################
# 两种DFS方法
# 一种是top down，也就是从根节点开始做先序遍历
# 另一种是bottom up，也就是把一棵树分为root + 两棵子树，先分别做两棵子树之后再合并，类似于分治法
##################################################

def dfs_top_down(root):
    result = []
    pre_order_recursive(root, result)
    return result

def dfs_bottom_up(root):
    result = []
    if root is None:
        return result
    left = dfs_bottom_up(root.left)
    right = dfs_bottom_up(root.right)
    return [root.val] + left + right

##################################################
# 两种DFS方法
# 一种是top down，也就是从根节点开始做先序遍历
# 另一种是bottom up，也就是把一棵树分为root + 两棵子树，先分别做两棵子树之后再合并，类似于分治法
##################################################

def bfs(tree):
    return tree.level_order()

##################################################
# 先序 + 中序 + 后序 + height
# 都是要遍历整棵树的
# 递归 + 不递归
##################################################

def pre_order_recursive(root, result):
    if(root is None):
        return
    result.append(root.val)
    pre_order_recursive(root.left, result)
    pre_order_recursive(root.right, result)       

def in_order_recursive(root, result):
    if(root is None):
        return
    in_order_recursive(root.left, result)
    result.append(root.val)
    in_order_recursive(root.right, result)       

def post_order_recursive(root, result):
    if(root is None):
        return
    post_order_recursive(root.left, result)
    post_order_recursive(root.right, result)       
    result.append(root.val)

def pre_order_norecur(root):
    if(root is None):
        return None
    result = []
    stack = []
    while(root is not None or len(stack) > 0):
        while(root is not None):
            result.append(root.val)
            stack.append(root)
            root = root.left
        root = stack.pop(-1)
        root = root.right
    return result

def in_order_norecur(root):
    if(root is None):
        return None
    result = []
    stack = []
    while(root is not None or len(stack) > 0):
        while(root is not None):
            stack.append(root)
            root = root.left
        root = stack.pop(-1)
        result.append(root.val)
        root = root.right
    return result

def post_order_norecur(root):
    if(root is None):
        return None
    result = []
    stack = []
    last_visited = None
    while(root is not None or len(stack) > 0):
        while(root is not None and root != last_visited):
            stack.append(root)
            root = root.left
        root = stack[-1]
        if(root.right is None or root.right == last_visited): # 说明以这个节点为root的这棵子树搜索完毕
            result.append(root.val)
            last_visited = root
            stack.pop(-1)
            root = None
        else:
            root = root.right
    return result

def height_recursive(root):
    if(root is None):
        return 0
    return max(height_recursive(root.left), height_recursive(root.right)) + 1

def height_norecur(root):
    # 基于层序遍历搜索高度，每次根据current_size和level_size搜索一层，高度响应的加1
    height = 0
    queue = [root]
    while(len(queue) > 0):
        height += 1
        level_size = len(queue)
        current_size = 0
        while(current_size < level_size):
            root = queue.pop(0)
            current_size += 1
            if(root.left):
                queue.append(root.left)
            if(root.right):
                queue.append(root.right)
    return height

if __name__ == '__main__':
    num_list = ['1','2','3','4','5','null','6','null','null','7','8']
    tree = Tree(num_list)
    print(tree.height(0))
    print(tree.height(1))
    print(tree.pre_order(0))
    print(tree.pre_order(1))
    print(dfs_top_down(tree.root))
    print(dfs_bottom_up(tree.root))
    print(tree.in_order(0))
    print(tree.in_order(1))
    print(tree.post_order(0))
    print(tree.post_order(1))
    print(tree.level_order())
    print(bfs(tree))