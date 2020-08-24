# My-Leetcode
## Note

- 回溯法：

  - 通过不停的选择，撤销选择，来穷尽所有可能性，最后将满足条件的结果全部返回
  - 是DFS的一种，实际上就是先序遍历
  - 是一种纯暴力搜索算法，时间复杂度一般是O(N!)
  - 模板：

  ```python
  result = []
  func backtrack(选择列表,路径):
      if 满足结束条件:
          result.add(路径)
          return
      for 选择 in 选择列表:
          做选择
          backtrack(选择列表,路径)
          撤销选择
  ```

- 分治法

  - 模板：

  ```
  func traversal(root *TreeNode) ResultType  {
      // nil or leaf
      if root == nil {
          // do something and return
      }
  
      // Divide
      ResultType left = traversal(root.Left)
      ResultType right = traversal(root.Right)
  
      // Conquer
      ResultType result = Merge from left and right
  
      return result
  }
  ```

- 链表
  - 相关的核心点
    - null 异常处理

    - dummy node 哑巴节点

    - 快慢指针

    - 插入一个节点到排序链表

    - 从一个链表中移除一个节点

    - 翻转链表

    - 合并两个链表

    - 找到链表的中间节点

      - 这两种方式不同点在于，一般用 fast=head.Next 较多，因为这样可以知道中点的上一个节点，可以用来删除等操作。

      - fast 如果初始化为 head.Next 则中点在 slow.Next
      - fast 初始化为 head,则中点在 slow

  - Useful functions

    ```python
    class Solutions:
        # reverse
        def reverseList(self, head: ListNode) -> ListNode:
            if(head is None or head.next is None):
                return head
            prev = None
            while(head is not None):
                head.next, head, prev = prev, head.next, head
            return prev
        
        # merge
        def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
            dummy = ListNode("dummy")
            head = dummy
            while(l1 is not None and l2 is not None):
                if(l1.val <= l2.val):
                    head.next, l1 = l1, l1.next
                else:
                    head.next, l2 = l2, l2.next
                head = head.next
            if(l1 is not None):
                head.next = l1
            if(l2 is not None):
                head.next = l2
            return dummy.next
        
        # find middle
        # 注意和has cycle的初始化有点不同
        def find_middle(self, head):
            slow = head
            fast = head.next
            while(fast is not None and fast.next is not None):
                slow = slow.next
                fast = fast.next.next
            return slow
       	
        # has circle
        def hasCycle(self, head: ListNode) -> bool:
            if(head is None or head.next is None):
                return False
            slow, fast = head, head
            while(fast is not None and fast.next is not None):
                slow = slow.next
                fast = fast.next.next
                if(slow == fast):
                    return True
            return False
    ```

    

