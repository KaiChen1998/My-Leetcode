class Solution:
    """
    Problems:
        Reverse a linked list from position m to n. Do it in one-pass.
        Note: 1 ≤ m ≤ n ≤ length of list.
    """
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode("dummy")
        dummy.next = head
        prev = dummy
        for _ in range(m - 1):
            prev = prev.next
        head = prev.next
        for _ in range(n - m):
            # 抓住head不放，因为head是一直向前走的
            follow = head.next
            head.next = follow.next
            follow.next = prev.next
            prev.next = follow
        return dummy.next