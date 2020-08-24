class Solution:
    """
    Useful functions: merge two lists
    注意仍然要处理两个链表的剩余部分
    """
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