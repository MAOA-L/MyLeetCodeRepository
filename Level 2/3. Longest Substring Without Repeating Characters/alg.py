# -*- coding: utf-8 -*-
"""
 @Time    : 2019/5/18 9:59
 @Author  : CyanZoy
 @File    : alg.py
 @Software: PyCharm
 @Describe: 3. 无重复字符的最长子串
 """


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
        """
        max_len = 0
        for i in range(len(s) - 1):
            for j in s[i:]:
                """去头"""
            for k in s[:-i]:
                """去尾"""


if __name__ == "__main__":
    # a = Solution().lengthOfLongestSubstring("dvdf")
    # print(a)
    print('d123456'[:-1])
