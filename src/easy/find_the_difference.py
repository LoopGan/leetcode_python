#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @author: LoopGan
    @contact: ganwei4955@gamil.com
    @time: 8/28/2018 4:50 PM
"""


class Solution:
    def findTheDifference(self, s, t):
        s_tmp = sorted(list(s))
        t_tmp = sorted(list(t))
        for i in range(len(s_tmp)):
            if s_tmp[i] != t_tmp[i]:
                return t_tmp[i]
        return t_tmp[-1]


if __name__ == "__main__":
    s = 'adc'
    t = 'abcd'
    ss = Solution()
    print(ss.findTheDifference(s, t))
    print("hello imp")
