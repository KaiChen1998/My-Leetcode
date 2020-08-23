class Solution:
    """
    Key point: 记得释放空间
    """
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        hash_table = []
        origin = head
        last = None
        while(head is not None):
            if(head.val in hash_table):
                last.next = head.next
                temp = head.next
                del(head)
                head = temp
            else:
                last = head
                hash_table.append(head.val)
                head = head.next
        return origin