#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @author: ganw
    @contact: wei.gan@emc.com
    @time: 8/15/2018 4:22 PM
"""

import math


class Solution:
    def reverse(self, x):
        if x > 0:
            str_value = str(x)[::-1]
            res = int(str_value)
        else:
            x = abs(x)
            str_value = str(x)[::-1]
            res = 0 - int(str_value)
        return 0 if (res > 2 ** 31 or res < -2 ** 31) else res


if __name__ == "__main__":
    ss = Solution()
    print(ss.reverse(123))
    print("hello imp")
