class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict = {}
        len_nums = len(nums)

        for i in range(len_nums):
            num = nums[i]
            compliment = target - num

            if compliment in seen_dict:
                return [seen_dict[compliment], i] #was already present so comes first

            seen_dict[num] = i

        return [] 