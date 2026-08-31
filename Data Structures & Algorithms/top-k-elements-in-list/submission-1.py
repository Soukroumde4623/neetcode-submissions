class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups ={}

        for i in range(len(nums)):
            if nums[i] not in groups:
                groups[nums[i]]= 0
            
            groups[nums[i]]+=1
        sorted_key = sorted(groups, key= groups.get,reverse=True)

        return sorted_key[:k]
        