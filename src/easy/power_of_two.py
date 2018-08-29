#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @author: LoopGan
    @contact: ganwei4955@gamil.com
    @time: 8/29/2018 5:42 PM
"""


class Solution:
    def isPowerOfTwo(self, n):
        r = 0
        while n > 2:
            p = n // 2
            r = n % 2
            n = p
        if r != 0:
            return False
        else:
            return True


if __name__ == "__main__":
    n = 5
    ss = Solution()
    print(ss.isPowerOfTwo(n))
    print("hello imp")
