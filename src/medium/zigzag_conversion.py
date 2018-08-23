#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @author: LoopGan
    @contact: ganwei4955@gamil.com
    @time: 8/22/2018 5:48 PM
"""
from collections import defaultdict


class Solution:
    def convert(self, s, numRows):
        tmp_unit = 2 * numRows - 2
        result = defaultdict(list)
        for i in range(len(s)):
            q = i // tmp_unit
            result[q].append(s[i])
        for k, v in result.items():
            for i in range(len(v)):
                in_r = i % numRows

        return result


if __name__ == "__main__":
    ss = Solution()
    s = 'PAYPALISHIRING'
    numRows = 3
    print(ss.convert(s, numRows))
    print("hello imp")
