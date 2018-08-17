#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @author: LoopGan
    @contact: ganwei4955@gamil.com
    @time: 8/17/2018 1:31 PM
"""



class Solution:
    def countAndSay(self, n):
        result = "1"
        for _ in range(n - 1):
            count = 1
            pre_value = result[0]
            current_result = ""
            for current_v in result[1:]:
                if current_v != pre_value:
                    current_result += str(count) + pre_value
                    count = 0
                    pre_value = current_v
                count += 1
            result = current_result + str(count) + pre_value
        return result

if __name__ == "__main__":
    ss = Solution()
    print(ss.countAndSay(5))
    print("hello imp")
