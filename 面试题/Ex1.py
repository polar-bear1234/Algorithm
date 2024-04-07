"""合并有序链表"""

list1 = [1,2,4,5]

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Solution:
    def structureList(self, nums):
        head = ListNode()
        for num in nums:
            pass


    def merge_list(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        dummy_head = ListNode()
        cur_node = dummy_head
        node1 = list1
        node2 = list2
        while node1 or node2:
            if not node1:
                cur_node.next = node2
                return dummy_head.next
            if not node2:
                cur_node.next = node1
                return dummy_head.next
            if node1.value < node2.value:
                cur_node.next = node1
                cur_node = cur_node.next
                node1 = node1.next
            else:
                cur_node.next = node2
                cur_node = cur_node.next
                node2 = node2.next
        return dummy_head.next

