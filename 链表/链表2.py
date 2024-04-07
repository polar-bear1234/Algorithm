class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val):
        dummy_head = ListNode(next=head)
        current = dummy_head
        while current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy_head.next


head = [1, 2, 6, 3, 4, 5, 6]
val = 6

func = Solution()
print(func.removeElements(head, val))
