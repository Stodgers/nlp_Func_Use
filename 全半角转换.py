# -*- coding: utf-8 -*-
# @Time : 2019-8-28 15:01:56
# @Author : Stodgers
# @FileName: 全半角转换.py
# @Software: PyCharm


def strQ2B(ustring):
    ss = []
    for s in ustring:
        rstring = ""
        for uchar in s:
            inside_code = ord(uchar)
            if inside_code == 12288:  # 全角空格直接转换
                inside_code = 32
            elif (inside_code >= 65281 and inside_code <= 65374):  # 全角字符（除空格）根据关系转化
                inside_code -= 65248
            rstring += chr(inside_code)
        ss.append(rstring)
    return "".join(ss)


print(strQ2B('VIｐＶＩｐｈａｉｈｄｌｂｉｃｌｗｗｈｈａ'))