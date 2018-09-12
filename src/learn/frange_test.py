#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @author: LoopGan
    @contact: ganwei4955@gamil.com
    @time: 9/12/2018 4:38 PM
"""


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


if __name__ == "__main__":
    for i in frange(0, 1, 0.2):
        print(i)
    print("hello imp")
