#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @author: LoopGan
    @contact: ganwei4955@gamil.com
    @time: 8/30/2018 5:03 PM
"""


class Solution:
    def reverseBit(self,n):
        pass

    def reverseBits_back(self, n):
        result = 0
        bin_start = bin(n)[2:]
        bin_target = str(bin_start)[::-1]
        lenght = len(bin_target)
        while lenght < 32:
            bin_target += '0'
            lenght += 1
        for i in range(lenght):
            result += int(bin_target[i]) * pow(2, lenght - i - 1)
        return result


if __name__ == "__main__":
    n = 43261596
    ss = Solution()
    print(ss.reverseBits(n))
    print("hello imp")
