#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @author: LoopGan
    @contact: ganwei4955@gamil.com
    @time: 8/29/2018 11:05 AM
"""


class Solution:
    def convertToTitle(self, n):
        q = []
        flag = 0
        while n > 26:
            reminder = n % 27
            quotient = n // 27
            q.append(quotient)
            n = reminder
            flag = 1
        if n <= 26:
            if flag == 1:
                reminder = reminder
            else:
                reminder = n
        print(reminder, q)

        return 'OK'


if __name__ == "__main__":
    n = 53
    ss = Solution()
    ss.convertToTitle(n)
    print("hello imp")
