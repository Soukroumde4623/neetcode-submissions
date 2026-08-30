class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elem ={}
        complement =0

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in elem:
                return [elem[complement], i]
            
            elem[nums[i]] = i
     