class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if(head is None or head.next is None):
            return head
        middle = self.find_middle(head)
        head_middle = middle.next
        middle.next = None
        left = self.sortList(head)
        right = self.sortList(head_middle)
        return self.merge(left, right)
    
    def find_middle(self, head):
        slow = head
        fast = head.next
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, l1, l2):
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