class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if(head is None):
            return head
        origin = head
        while(head is not None):
            new = Node(head.val, head.next, None)
            head.next = new
            head = head.next.next
        head = origin
        while(head is not None):
            head.next.random = None if head.random is None else head.random.next 
            head = head.next.next
        head = origin
        dummy = Node('0')
        head_dummy = dummy
        while(head is not None):
            head_dummy.next = head.next
            head_dummy = head_dummy.next
            head.next = head.next.next
            head = head.next
        return dummy.next