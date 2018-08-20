#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @author: LoopGan
    @contact: ganwei4955@gamil.com
    @time: 8/20/2018 2:41 PM
"""


class Solution:
    def fourSum(self, nums, target):
        def findNSum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:
                return
            if N == 2:
                left, right = 0, len(nums) - 1
                while left < right:
                    current_sum = nums[left] + nums[right]
                    if current_sum == target:
                        results.append(result + [nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
            else:
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                        findNSum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)

        results = []
        findNSum(sorted(nums), target, 4, [], results)
        return results


def fourSum_bck(self, nums, target):
    if len(nums) < 4:
        return []
    else:
        all_con = []
        for i in range(len(nums) - 2):
            tmp_i = nums[i]
            for j in range(i + 1, len(nums) - 1):
                tmp_j = nums[j]
                for k in range(j + 1, len(nums)):
                    tmp_k = nums[k]
                    rest_target = target - sum([tmp_i, tmp_j, tmp_k])
                    tmp_index = [i for i in range(len(nums))]
                    tmp_index.remove(i)
                    tmp_index.remove(j)
                    tmp_index.remove(k)
                    rest_nums = [nums[i] for i in tmp_index]
                    if rest_target in rest_nums:
                        target_array = sorted([tmp_i, tmp_j, tmp_k, rest_target])
                        if target_array not in all_con:
                            all_con.append(target_array)
        return all_con


if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    ss = Solution()
    print(ss.fourSum(nums, target))
    print("hello imp")
