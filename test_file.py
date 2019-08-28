# -*- coding: utf-8 -*-
# @Author : Stodgers
# @Time : 2019-8-28 15:19:34
# @FileName: test_file.py
# @Software: PyCharm
RAW_DATA_FPATH = "T-news_sohusite_xml_xml.txt"
MODEL_PREFIX = "sp10m.cased.v3"
VOC_SIZE = 9000
COVERAGE = 0.99995
SPM_COMMAND = ('--input={} '
               '--model_prefix={} '
               '--vocab_size={} '

               '--character_coverage={} '
               '--shuffle_input_sentence=true '
               '--model_type=unigram '
               '--control_symbols=\<cls\>,\<sep\>,\<pad\>,\<mask\>,\<eod\> '
               '--user_defined_symbols=<eop>,.,(,),",-,–,£,€ ').format(
    RAW_DATA_FPATH,
    MODEL_PREFIX,
    VOC_SIZE,
    COVERAGE)
print(SPM_COMMAND)