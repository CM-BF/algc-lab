"""
Author: Citrine
Date: 14th November, 2018
Description: 最长公共子序列问题：手动输入两条字符串序列，输出它们的最长公共子序列。
最长公共子序列问题和调研报告：上机题测试样例：输入ABCBDAB和BDCABA；关于调研报告：和实验报告一起提交，回答：
1. 现在的LCS时间复杂度最好的算法是什么？2. 具体的时间复杂度，算法思路（自己组织语言，请勿完全摘抄原文），以及给出参考文献。
"""
import copy
import numpy as np


def lcs_length(x, y):
    m = len(x)
    n = len(y)
    temp1 = [0 for i in range(n + 1)]
    c = [copy.deepcopy(temp1) for i in range(m + 1)]
    temp1 = [' ' for i in range(n + 1)]
    b = [copy.deepcopy(temp1) for i in range(m + 1)]
    for i in range(m + 1):
        c[i][0] = 0
    for j in range(n + 1):
        c[0][j] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = '\\'
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = '|'
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = '--'
    return c, b

def print_lcs(b, x, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == '\\':
        print_lcs(b, x, i - 1, j - 1)
        print(x[i - 1])
    elif b[i][j] == '|':
        print_lcs(b, x, i - 1, j)
    else:
        print_lcs(b, x, i, j - 1)


if __name__=='__main__':
    x = 'ABCBDAB'
    y = 'BDCABA'
    c, b = lcs_length(x, y)
    print_lcs(b, x, len(x), len(y))
    print(np.array(c), '\n', np.array(b))


