class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if(head is None or head.next is None):
            return head
        prev = None
        while(head is not None):
            head.next, head, prev = prev, head.next, head
        return prev