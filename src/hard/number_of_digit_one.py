#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @author: LoopGan
    @contact: ganwei4955@gamil.com
    @time: 9/5/2018 1:20 PM
"""


class Solution:
    def countDigitOne(self, n):
        result = 0
        for i in range(1, n + 1):
            result += str(i).count('1')
        return result


if __name__ == "__main__":
    n = 824883294
    len(n)
    ss = Solution()
    print(ss.countDigitOne(n))
    print("hello imp")
