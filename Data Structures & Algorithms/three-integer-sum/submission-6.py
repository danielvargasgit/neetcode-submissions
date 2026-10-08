class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = 0 - nums[i]
            j = i + 1
            k = len(nums) - 1

            while j < k:
                current_sum = nums[j] + nums[k]
                if current_sum == target:
                    output.append([-target, nums[j], nums[k]])
                    k = k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j = j + 1
                    while j < k and nums[k] == nums[k + 1]:
                        k = k - 1
                elif current_sum < target:
                    j = j + 1
                else:
                    k = k - 1
        return output


                            