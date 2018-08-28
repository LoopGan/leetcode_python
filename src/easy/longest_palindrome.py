#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @author: LoopGan
    @contact: ganwei4955@gamil.com
    @time: 8/28/2018 5:15 PM
"""


class Solution:
    def longestPalindrome(self, s):
        s_list = list(s)
        dict_tmp = {}
        for i in s:
            if i not in dict_tmp:
                dict_tmp[i] = s_list.count(i)
        result = 0
        flag = 0
        for k, v in dict_tmp.items():
            if v % 2 == 1:
                result += v // 2 * 2
                flag = 1
            else:
                result += v
        if flag:
            result += 1
        return result


if __name__ == "__main__":
    s = 'abccccdd'
    ss = Solution()
    print(ss.longestPalindrome(s))
    print("hello imp")
