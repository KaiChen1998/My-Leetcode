class Solution:
    """
    Problems:
        Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
        You should preserve the original relative order of the nodes in each of the two partitions.
    Solutions:
        大的和小的分别用独立的链表存储之后再合并
    """
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode("dummy")
        dummy.next = head
        prev = dummy
        dummy_new = ListNode("dummy")
        head_new = dummy_new
        while(head is not None):
            if(head.val < x):
                head, prev = head.next, prev.next
            else:
                prev.next = head.next
                head.next = None
                head_new.next = head
                head_new = head_new.next
                head = prev.next
        prev.next = dummy_new.next
        return dummy.next