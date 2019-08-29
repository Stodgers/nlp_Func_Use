# -*- coding: utf-8 -*-
# @Time : 2019-8-28 15:01:56
# @Author : Stodgers
# @FileName: Q2B2Q.py
# @Software: PyCharm

class Q2B2Q:
    def strQ2B(self,ustring):
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

    def strB2Q(self,ustring):
        """半角转全角"""
        rstring = ""
        for uchar in ustring:
            inside_code=ord(uchar)
            if inside_code == 32:                                 #半角空格直接转化
                inside_code = 12288
            elif inside_code >= 32 and inside_code <= 126:        #半角字符（除空格）根据关系转化
                inside_code += 65248
            rstring += chr(inside_code)
        return rstring

# kk = Q2B2Q()
# print(kk.strQ2B('哈哈哈哈123Ab'))
# print(kk.strB2Q('哈哈哈哈123Ab'))
