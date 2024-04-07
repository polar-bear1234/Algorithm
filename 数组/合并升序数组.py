"""将两个升序的数组合并，合并后的数组保持升序，设计时间复杂度尽可能低的算法"""
# 空间复杂度：O(1)
# 时间复杂度：O(n)


def mergeLists(l1, l2):
    j = len(l2) - 1   # l2 倒序遍历
    i = len(l1) - 1
    while j >= 0:
        if l2[j] <= l1[i]:
            i -= 1
            continue
        else:
            l1.insert(i + 1, l2[j])
            j -= 1
    return l1


list1 = [1,3,5,7,9]
list2 = [2,2,4,6,7,8,8,8,8]
result = mergeLists(list1, list2)
print(result)