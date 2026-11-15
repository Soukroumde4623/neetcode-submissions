class Solution:
    def search(self, nums: List[int], target: int) -> int:

        fin = len(nums)-1
        debut = 0
        while debut<=fin:
            mid = (fin + debut)//2

            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                fin = mid-1
            else:
                debut = mid+1
        return -1