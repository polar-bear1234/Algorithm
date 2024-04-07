"""
题目：
    编写代码，移除排序链表中的重复节点。保留最开始出现的节点。
输入：[1, 1, 1, 1, 2]
输出：[1, 2]
题目：
    编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。
输入：[1, 2, 3, 3, 2, 1]
输出：[1, 2, 3]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next


class Solution:
    def structListNode(self, nums):
        head = ListNode(nums[0])
        cur = head
        for num in nums[1:]:
            node = ListNode(num)
            cur.next = node
            cur = cur.next
        result = self.print_value(head)
        print(result)
        return head

    def remove1(self, nums):
        head = self.structListNode(nums)
        dummy_head = ListNode()
        dummy_head.next = head
        pre_head = dummy_head
        cur_head = head
        while cur_head.next:
            if pre_head.value != cur_head.value:
                pre_head = cur_head
                cur_head = cur_head.next
            else:
                cur_head = cur_head.next
                pre_head.next = cur_head
        result = self.print_value(dummy_head.next)
        print("去重后如下:------", "\n", result)
        return dummy_head.next

    def remove2(self, nums):
        head = self.structListNode(nums)
        dummy_head = ListNode()
        dummy_head.next = head
        pre_node = dummy_head
        cur_node = head
        hash_set = set()
        while cur_node:
            if cur_node.value not in hash_set:
                hash_set.add(cur_node.value)
                pre_node = cur_node
                cur_node = cur_node.next
            else:
                cur_node = cur_node.next
                pre_node.next = cur_node
        result = self.print_value(dummy_head.next)
        print("去重后如下:------", "\n", result)
        return dummy_head.next

    def print_value(self, head):
        node = head
        output = ""
        while node:
            output += str(node.value)
            output += " -> "
            node = node.next
        return output[:-4]


nums = [1, 1, 1, 1, 2, 3, 3, 4]
nums2 = [1, 2, 3, 3, 2, 1]
f = Solution()
result = f.remove1(nums)
result2 = f.remove2(nums2)

