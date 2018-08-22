#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @author: LoopGan
    @contact: ganwei4955@gamil.com
    @time: 8/22/2018 9:35 AM
"""


def decimalToAny(n, x):
    tmp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    result_tmp = []
    while True:
        quotient = n // x
        remainder = n % x
        result_tmp.append(remainder)
        if quotient == 0:
            break
        n = quotient
    result_tmp.reverse()
    result = []
    for i in result_tmp:
        result.append(tmp[i])
    return ''.join([str(i) for i in result])


if __name__ == "__main__":
    a = 10
    print(decimalToAny(a, 16))
    print(hex(a))
    print("hello imp")
