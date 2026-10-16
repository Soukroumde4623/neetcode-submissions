class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        tab = sorted(nums, key=None, reverse=False)
        current_size = 1;
        maximum=1;
        for i in range(len(tab)-1):
            if tab[i+1]==tab[i]:
                continue

            elif tab[i+1]==tab[i]+1 :
                current_size+=1
            else:
                maximum = max(current_size,maximum)
                current_size=1

        return max(maximum, current_size)

