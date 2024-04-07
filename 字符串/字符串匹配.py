class Solution:
    def getNext(self, next, s):
        j = 0
        next[0] = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1
            next[i] = j

    def strStr(self, hystack, needle):
        if len(needle) == 0:
            return 0
        next = [0] * len(needle)
        self.getNext(next, needle)
        j = 0
        for i in range(len(hystack)):
            while j > 0 and hystack[i] != needle[j]:
                j = next[j - 1]
            if hystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1
        return -1

    def solution(self, hystack, needle):
        for i in range(len(hystack)):
            if len(hystack) - i < len(needle):
                break
            for j in range(len(needle)):
                if hystack[i+j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1


# hystack = "abcdabcd"
# needle = "acdb"
# function = Solution()
# print(function.strStr(hystack, needle))
# print(function.solution(hystack, needle))

s = "ac"
g = Solution()
next = [0] * len(s)
g.getNext(next, s)
print(next)
ind = next.index(max(next))
print(next[ind - 2 * max(next):ind+1])
print(s[ind - 2 * max(next):ind+1])
