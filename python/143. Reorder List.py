class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if(head is None or head.next is None):
            return head
        middle = self.find_middle(head)
        prev_middle = middle
        head_middle = prev_middle.next
        middle.next = None
        temp = None
        while(head_middle is not None):
            temp = head_middle.next
            head_middle.next = prev_middle if(prev_middle != middle) else None
            prev_middle, head_middle = head_middle, temp
        while(head is not None and prev_middle is not None):
            temp = head.next
            head.next = prev_middle
            head = temp
            temp = prev_middle.next
            prev_middle.next = head
            prev_middle = temp
    
    def find_middle(self, head):
        slow = head
        fast = head.next
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        return slow