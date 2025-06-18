class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        prefix = [nums[0]]
        for i in range(len(nums) - 1):
            prefix.append(prefix[i] * nums[i + 1])

        suffix = [1] * (len(nums) + 1)
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = (suffix[i + 1] * nums[i])

        for i in range(len(nums)):
            if i == 0:
                answer[i] = suffix[i + 1]
            elif i == len(nums) - 1:
                answer[i] = prefix[i - 1]
            else:
                answer[i] = prefix[i - 1] * suffix[i + 1]
        
        return answer
