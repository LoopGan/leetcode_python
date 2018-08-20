#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @author: LoopGan
    @contact: ganwei4955@gamil.com
    @time: 8/20/2018 5:26 PM
"""


class Solution:
    def findRepeatedDnaSequence(self, s):
        left, right = 0, len(s) - 1
        result = []
        while left < right:
            if s[left:left + 10] == s[right - 10:right] and (left + 10) < (right - 10):
                result.append(s[left:left + 10])

        return s


if __name__ == "__main__":
    print("hello imp")
