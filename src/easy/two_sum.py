#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @author: LoopGan
    @contact: ganwei4955@gmail.com
    @time: 8/15/2018 10:36 AM
"""


class Solution(object):
    def twoSum(self, nums, target):
        for i, num in enumerate(nums):
            print(i, num)
            complement = target - num
            if complement in nums[i + 1:]:
                return [i, nums.index(complement, i + 1)]
        return None


if __name__ == "__main__":
    ss = Solution()
    print(ss.twoSum([4, 3, 3], 6))
