class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        deja_vu = {}

        for idx, num in enumerate(numbers, start=1):
            x = target - num

            if x in deja_vu:
                return [deja_vu[x], idx]

            deja_vu[num] = idx 