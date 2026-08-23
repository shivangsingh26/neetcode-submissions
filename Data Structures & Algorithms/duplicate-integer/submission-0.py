class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums_set = set()
        for val in nums:

            if val in nums_set:
                return True
            else:
                nums_set.add(val)
        return False