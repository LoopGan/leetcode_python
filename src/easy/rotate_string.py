#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    @author: loopgan
    @contact: ganwei4955@gmail.com
    @time: 18-10-10 上午12:58
"""


class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        else:
            if len(A) == 0:
                return True
            for i in range(len(B), 0, -1):
                if i == 0:
                    return False
                if B[0:i] in A:
                    if B[i:] in A:
                        return True
                    else:
                        return False
                else:
                    return False


if __name__ == "__main__":
    A = 'abcde'
    B = 'cdeab'
    ss = Solution()
    print(ss.rotateString(A, B))
    print("Hello imp")
