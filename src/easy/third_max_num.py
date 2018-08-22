#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @author: LoopGan
    @contact: ganwei4955@gamil.com
    @time: 8/22/2018 10:53 AM
"""


class Solution:
    def thirdMax(self, nums):
        nums.sort()
        tmp = []
        for i in nums[::-1]:
            if i not in tmp and len(tmp) < 3:
                tmp.append(i)
        if len(tmp) == 3:
            return tmp[-1]
        else:
            return tmp[0]


if __name__ == "__main__":
    ss = Solution()
    nums = [2, 2, 3]
    print(ss.thirdMax(nums))
    print("hello imp")
