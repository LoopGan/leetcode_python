#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    @author: loopgan
    @contact: ganwei4955@gmail.com
    @time: 18-10-10 上午12:24
"""


class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        return ['%d:%02d' % (h, m) for h in range(12) for m in range(60) if (bin(h) + bin(m)).count('1') == num]


if __name__ == "__main__":
    num = 1
    ss = Solution()
    print(ss.readBinaryWatch(num))
    # print("Hello imp")
