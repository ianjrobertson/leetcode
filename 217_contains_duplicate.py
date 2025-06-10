class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        values = dict()
        for num in nums:
            if num in values.keys():
                return True
            else:
                values[num] = 1
        return False
