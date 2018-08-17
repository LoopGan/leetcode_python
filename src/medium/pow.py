#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @author: LoopGan
    @contact: ganwei4955@gamil.com
    @time: 8/17/2018 10:12 AM
"""


class Solution:
    def myPow(self, x, n):
        if n > 0:
            if n == 1:
                return x
            else:
                return x * self.myPow(x, n - 1)
        elif n == 0:
            return 1
        else:
            if n == -1:
                return float(1 / x)
            else:
                return 1 / (x * (1 / self.myPow(x, n + 1)))
        pow(2,3)


if __name__ == "__main__":
    ss = Solution()
    print(ss.myPow(1.001, 998))
    print("hello imp")
