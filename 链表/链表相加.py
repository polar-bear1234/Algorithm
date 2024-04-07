"""两个链表相加"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def strucList(self, nums):
        dummy_head = ListNode(0)
        cur = dummy_head
        for num in nums:
            cur.next = ListNode(num)
            cur = cur.next
        return dummy_head.next

    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    def printList(self, head: ListNode) -> str:
        result = ""
        while head:
            result += str(head.val)
            result += " -> "
            head = head.next
        return result[:-4]

    def addList(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1
        head1 = self.reverseList(head1)
        head2 = self.reverseList(head2)
        print('head1反转后:', self.printList(head1))
        print('head2反转后：', self.printList(head2))
        carry = 0         # 进位值
        dummy_head = ListNode(0)
        cur = dummy_head
        while head1 != None or head2 != None or carry != 0:
            val1 = 0 if head1 == None else head1.val
            val2 = 0 if head2 == None else head2.val
            addSum = val1 + val2 + carry
            carry = int(addSum/10)
            addSum = addSum % 10
            cur.next = ListNode(addSum)
            cur = cur.next
            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next
        return dummy_head.next

    def main(self, nums1, nums2):
        head1 = self.strucList(nums1)
        head2 = self.strucList(nums2)
        print('head1反转前:', self.printList(head1))
        print('head2反转前：', self.printList(head2))
        new_head = self.addList(head1, head2)
        result = self.reverseList(new_head)
        print('Result:', self.printList(result))
        return result


nums1 = [9, 3, 7]
nums2 = [6, 3]
g = Solution()
result = g.main(nums1, nums2)
print(result)
