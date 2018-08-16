#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @author: LoopGan
    @contact: ganwei4955@gamil.com
    @time: 8/16/2018 1:35 PM
"""


class Solution:
    def __init__(self):
        self.INT_MIN = -2 ** 31
        self.INT_MAX = 2 ** 31 - 1

    def myAtoi(self, x):
        x = x.lstrip()
        x_dict = {}
        for i in range(0, len(x)):
            x_dict[i] = x[i]
        num_index = []
        other_index = []
        minus_index = []
        plus_index = []
        for k, v in x_dict.items():
            if v == '-':
                minus_index.append(k)
            elif v == '+':
                plus_index.append(k)
            elif v.isnumeric():
                num_index.append(k)
            else:
                other_index.append(k)
        if len(other_index) == 0:
            result_index = num_index
        else:
            result_index = [i for i in num_index if i < min(other_index)]
        if len(result_index):
            for i in minus_index:
                if i > min(result_index):
                    result_index = [j for j in result_index if j < i]
                    break
            for i in plus_index:
                if i > min(result_index):
                    result_index = [j for j in result_index if j < i]
                    break
            if 0 not in result_index:
                if x.startswith('+'):
                    result = int(''.join([x[i] for i in result_index]))
                    for i in range(0, len(plus_index) - 1):
                        for j in range(1, len(plus_index)):
                            if abs(plus_index[i] - plus_index[j]) == 1:
                                return 0
                    for i in plus_index:
                        for j in minus_index:
                            if abs(i - j) == 1:
                                return 0
                elif x.startswith('-'):
                    result = 0 - int(''.join([x[i] for i in result_index]))
                    for i in range(0, len(minus_index) - 1):
                        for j in range(1, len(minus_index)):
                            if abs(minus_index[i] - minus_index[j]) == 1:
                                return 0
                    for i in plus_index:
                        for j in minus_index:
                            if abs(i - j) == 1:
                                return 0
            else:
                result = int(''.join([x[i] for i in result_index]))
            if result > self.INT_MAX:
                return self.INT_MAX
            elif result < self.INT_MIN:
                return self.INT_MIN
            else:
                return result
        else:
            return 0


if __name__ == "__main__":
    ss = Solution()
    print(ss.myAtoi("-3-"))
    print("hello imp")
