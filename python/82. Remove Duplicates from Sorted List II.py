class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = TreeNode('dummy')
        dummy.next = head
        last = head = dummy
        while(head is not None):
            if(head.next is not None and head.val == head.next.val):
                val = head.val
                while(head is not None and head.val == val):
                    temp = head.next
                    del(head)
                    head = temp
                last.next = head
            else:
                last = head
                head = head.next
        return dummy.next