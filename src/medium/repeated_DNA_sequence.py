#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @author: LoopGan
    @contact: ganwei4955@gamil.com
    @time: 8/20/2018 5:26 PM
"""


class Solution:
    def findRepeatedDnaSequences(self, s):
        results_dict = {}
        res = set()
        for i in range(len(s) - 9):
            if s[i:i + 10] in results_dict:
                res.add(s[i:i + 10])
            results_dict[s[i:i + 10]] = 1
        return list(res)


if __name__ == "__main__":
    ss = Solution()
    s = 'AAAAAAAAAAAA'
    print(ss.findRepeatedDnaSequences(s))
    print("hello imp")
