#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @author: ganw
    @contact: wei.gan@emc.com
    @time: 8/16/2018 9:23 AM
"""


class Solution:
    def addTowNumbers(self, l1, l2):
        l3 = None
        a = 0
        while l1 or l2 or a:
            if l1:
                a += l1.val
                l1 = l1.next

            if l2:
                a += l2.val
                l2 = l2.next

            if l3:
                l3.next = ListNode(a % 10)
                l3 = l3.next
            else:
                l0 = ListNode(a % 10)
                l3 = l0

            a = a // 10

        return l0


if __name__ == "__main__":
    print("hello imp")
