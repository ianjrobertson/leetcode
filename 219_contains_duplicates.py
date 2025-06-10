class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        values = dict()

        for i in range(len(nums)):
            if nums[i] in values.keys():
                if abs(i - values[nums[i]]) <= k:
                    return True
                else:
                    values[nums[i]] = i
            else:
                values[nums[i]] = i
        return False
