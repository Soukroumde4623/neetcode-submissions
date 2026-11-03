class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        tab = set(nums)

        maximum= 0
        for m in tab:
            if m - 1 not in tab:
                current_num=m
                current_len =1
            
                while current_num + 1 in tab:
                     current_num +=1
                     current_len +=1
                maximum = max(maximum, current_len)
        return maximum

        # if not nums:
        #     return 0
        # tab = sorted(nums, key=None, reverse=False)
        # current_size = 1;
        # maximum=1;
        # for i in range(len(tab)-1):
        #     if tab[i+1]==tab[i]:
        #         continue

        #     elif tab[i+1]==tab[i]+1 :
        #         current_size+=1
        #     else:
        #         maximum = max(current_size,maximum)
        #         current_size=1

        # return max(maximum, current_size)

