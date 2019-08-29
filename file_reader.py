# -*- coding: utf-8 -*-
# @Author : Stodgers
# @Time : 2019-8-29 14:16:03
# @FileName: file_reader.py
# @Software: PyCharm
import pandas as pd
import numpy as np

class file_reader:
    def text_reader(self,path):
        with open(path,errors='ignore',encoding='utf-8') as f:
            data = []
            for i in f.readlines():
                temp = i.strip()
                '''
                    可以添加额外处理
                '''
                data.append(temp)
            return data

    def csv_reader(self,path,header,encod):
        with pd.read_csv(path,header=header,encoding=encod).values.tolist() as f:
            temp = f
            '''
                可以添加额外处理
            '''
            return temp
    def excel_reader(self,path,header,encod):
        with pd.read_excel(path,header=header,encoding=encod).values.tolist() as f:
            temp = f
            '''
                可以添加额外处理
            '''
            return temp