#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @author: LoopGan
    @contact: ganwei4955@gamil.com
    @time: 8/22/2018 10:53 AM
"""


class Solution:
    def thirdMax_back(self, nums):
        nums.sort()
        tmp = []
        for i in nums[::-1]:
            if i not in tmp and len(tmp) < 3:
                tmp.append(i)
        if len(tmp) == 3:
            return tmp[-1]
        else:
            return tmp[0]

    def thirdMax(self, nums):
        print(set(sorted(nums)))
        return sorted(set(nums))[-3] if len(set(nums)) >= 3 else max(nums)


if __name__ == "__main__":
    ss = Solution()
    nums = [2345, 2300, -1213, 9178, 2980, -6607, -2535, 7676]
    print(ss.thirdMax(nums))
    print("hello imp")
