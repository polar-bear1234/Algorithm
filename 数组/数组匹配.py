"""
题目：
    给你一个整数数组 arr ，数组中的每个整数 互不相同 。另有一个由整数数组构成的数组 pieces，其中的整数也 互不相同 。请你以 任意顺序 连接 pieces 中的数组以形成 arr 。
    但是，不允许 对每个数组 pieces[i] 中的整数重新排序。
    如果可以连接 pieces 中的数组形成 arr ，返回 true ；否则，返回 false 。
输入：arr = [15,88], pieces = [[88],[15]]
输出：true
"""

class Solution:
    def searchArr(self, arr, pieces):
        hash_map = {num[0]: i for i, num in enumerate(pieces)}
        idx = 0
        while idx < len(arr):
            if arr[idx] not in hash_map:
                return False
            for piece in pieces[arr[idx]]:
                if piece == arr[idx]:
                    idx += 1
                else:
                    return False
        return True


class Solution:
    def canFormArray(self, arr, pieces):
        MIN = float('inf')
        for piece in pieces:
            n = len(piece)
            p = piece[0]
            if p in arr:
                ind = arr.index(p)
                if piece != arr[ind:ind+n]:
                    return False
                else:
                    for i in range(n - 1, -1, -1):
                        arr[ind+i] = MIN
            else:
                return False
        return arr == [MIN] * len(arr)

    def canFormArray2(self, arr, pieces):
        '''方法二: 哈希表+排序'''
        hashmap = {piece[0]: i for i, piece in enumerate(pieces)}
        idx = 0
        while idx < len(arr):
            if arr[idx] not in hashmap:
                return False
            for num in pieces[hashmap[arr[idx]]]:
                if num != arr[idx]:
                    return False
                idx += 1
        return True
