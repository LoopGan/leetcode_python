#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    @author: loopgan
    @contact: ganwei4955@gmail.com
    @time: 18-9-5 上午12:01
"""


class Solution:
    def findErrorNums(self, nums):
        tmp = [i + 1 for i in range(len(nums))]
        r = 0
        zz = []
        for i in nums:
            if i in zz:
                r = i
            else:
                zz.append(i)
        lack = list(set(tmp).difference(set(nums)))[0]
        return r, lack


if __name__ == "__main__":
    s = [1, 2, 2, 4]
    ss = Solution()
    print(ss.findErrorNums(s))
    print("Hello imp")
