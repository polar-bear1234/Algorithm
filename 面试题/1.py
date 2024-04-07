class Solution:
    def count_climbable(self , hill_map , strength):
        i = 1
        size = len(hill_map)
        while i < size:
            if hill_map[i] != 0 and hill_map[i-1] == 0:
                break
            i += 1
        num = 0
        count = 0
        while i < size:
            if hill_map[i] == 0:
                if num <= strength:
                    count += 1
                num = 0
                while i < size and hill_map[i] == 0:
                    i += 1
            if i < size and hill_map[i] > hill_map[i-1]:
                num += (hill_map[i] - hill_map[i-1]) * 2
                i += 1
            elif i < size and hill_map[i] < hill_map[i-1]:
                num += (hill_map[i-1] - hill_map[i]) * 1
                i += 1
        return count

hill_map = [0,1,4,3,1,0,0,1,2,3,0,2,1,0,1,2,0,1,0]
strength = 36

g = Solution()
result = g.count_climbable(hill_map, strength)
print(result)