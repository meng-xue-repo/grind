############### Slow ###############
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                        return [i, j]
        return []


############### Fast ###############
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for index in range(len(nums)):
            val = nums[index]
            complement = target - val

            # Do not need to consider if they are the same element, because it's impossible
            if complement in dic:
                return [index, dic[complement]]
            
            dic[val] = index

        return []
