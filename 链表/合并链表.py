"""
题目：
    给你一个链表数组，每个链表都已经按升序排列。请你将所有链表合并到一个升序链表中，返回合并后的链表
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6

输入：lists = []
输出：[]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def printList(self, head):
        result = ""
        while head:
            result += str(head.val)
            result += " -> "
            head = head.next
        return result[:-4]

    def strucList(self, nums_list):
        head_list = []
        for nums in nums_list:
            dummy_head = ListNode(0)
            cur = dummy_head
            for num in nums:
                cur.next = ListNode(num)
                cur = cur.next
            head_list.append(dummy_head.next)
        return head_list

    def mergeHeads(self, nums_list):
        orderdict = {}
        head_list = self.strucList(nums_list)
        for head in head_list:
            while head:
                if head.val not in orderdict:
                    orderdict[head.val] = 1
                else:
                    orderdict[head.val] += 1
                head = head.next
        dummy_head = ListNode(0)
        cur = dummy_head
        keysort = sorted(orderdict.keys())
        sorted_dict = {key: orderdict[key] for key in keysort}
        print("ordereddict is :", sorted_dict)
        for k, v in sorted_dict.items():
            while v:
                cur.next = ListNode(k)
                cur = cur.next
                v -= 1
        print(self.printList(dummy_head.next))
        return dummy_head.next


lists = [[1,4,5],[1,3,4],[2,6]]
g = Solution()
head_list = g.strucList(lists)
print_head_list = [g.printList(head) for head in head_list]
print(print_head_list)
result = g.mergeHeads(lists)
print(result)
