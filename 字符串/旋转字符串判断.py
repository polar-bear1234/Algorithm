class Solution:
    def getNext(self, next, s):
        j = 0
        next[j] = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1
            next[i] = j

    def isFlipedString(self, s1, s2):
        if not s1 and not s2:
            return True
        if len(s1) != len(s2):
            return False
        hash_map = {}
        for s in s1:
            if s not in hash_map:
                hash_map[s] = 1
            else:
                hash_map[s] += 1
        for s in s2:
            if s not in hash_map:
                return False
            else:
                hash_map[s] -= 1
        for value in hash_map.values():
            if value != 0:
                return False
        s3 = s1 + s1
        next = [0] * len(s2)
        self.getNext(next, s2)
        j = 0
        for i in range(len(s3)):
            while j > 0 and s3[i] != s2[j]:
                j = next[j - 1]
            if s3[i] == s2[j]:
                j += 1
            if j == len(s2):
                return True
        return False


s1 = "abcdabcd"
s2 = "acdb"
f = Solution()
result = f.isFlipedString(s1, s2)
print(result)