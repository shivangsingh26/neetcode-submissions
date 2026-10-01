class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen_dict = {}

        for i in range(n):
            compliment = target - nums[i]

            if compliment in seen_dict:
                return [seen_dict[compliment] , i]

            seen_dict[nums[i]] = i

        return []      