class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def strucList(self, nums):
        head = ListNode(nums[0])
        cur = head
        for num in nums[1:]:
            node = ListNode(num)
            cur.next = node
            cur = cur.next
        return head

    def reverseList(self, nums):
        head = self.strucList(nums)
        print("反转前：", self.print_value(head))
        pre = None
        current = head
        while current:
            tmp = current.next
            current.next = pre
            pre = current
            current = tmp
        print("反转后：", self.print_value(pre))
        return pre

    def print_value(self, head):
        node = head
        output = ""
        while node:
            output += str(node.val)
            output += " -> "
            node = node.next
        return output[:-4]


head = [1, 2, 3, 4]
g = Solution()
al = g.reverseList(head)
print(al)