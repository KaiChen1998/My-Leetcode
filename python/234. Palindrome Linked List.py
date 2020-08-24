class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if(head is None or head.next is None):
            return True
        middle = self.find_middle(head)
        right = self.reverse(middle.next)
        middle.next = None
        del(middle)
        while(right is not None and head is not None):
            if(right.val != head.val):
                return False
            else:
                right, head = right.next, head.next
        return True

    def reverse(self, head):
        prev = None
        while(head is not None):
            temp = head.next
            head.next = prev
            prev, head = head, temp
        return prev

    def find_middle(self, head):
        slow, fast = head, head.next
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        return slow