class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while right > left:
            # Note the "//" operator
            mid = (left + right)//2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                # Shift mid
                right = mid - 1
            else:
                # Shift mid
                left = mid + 1

        # left == right
        return left if nums[left] == target else -1
