#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @author: LoopGan
    @contact: ganwei4955@gamil.com
    @time: 8/16/2018 1:21 PM
"""


class Solution:
    def isPalindrome(self, x):
        org = str(x)
        rev = org[::-1]
        return org == rev
        # if str(x) == str(x)[::-1]:
        #     return True
        # else:
        #     return False


if __name__ == "__main__":
    ss = Solution()
    print(ss.isPalindrome(1001))
    print("hello imp")
