class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if(head is None or head.next is None):
            return None
        fast, slow = head, head
        while(fast is not None and fast.next is not None):
            fast = fast.next.next
            slow = slow.next
            if(slow == fast):
                break
        if(fast != slow):
            return None
        while(slow != head):
            slow = slow.next
            head = head.next
        return head