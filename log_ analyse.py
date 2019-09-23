import pandas as pd
import numpy as np
import os
import requests,re
import urllib
def url_cat(h):
    url = 'http://ip.tool.chinaz.com/' + h
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
    print(url)
    html = requests.get(url, headers=head)
    # html.content.decode('gb2312')
    #print(html.encoding)
    #print(html.apparent_encoding)
    html = html.text.encode(html.encoding).decode(html.apparent_encoding)

    #print(html)
    ren = re.compile(r'<span class="Whwtdhalf w50-0">(.*?)</span>')

    html_list = re.findall(ren, html)
    if len(html_list)!=0:
        return html_list[1]
    else:
        return 'error'
path = u'c:\\Users\CCP\Desktop\log.txt'
with open(path,errors='ignore') as f:
    tt = [i.split("-")[0].strip() for i in f.readlines()]
    dic = {}
    for k,v in enumerate(tt):
        if v not in dic:
            dic[v] = 1
        else:
            dic[v] += 1
    lans =[[k,v] for k,v in dic.items()]
    lans = sorted(lans,key=lambda x:x[1],reverse=True)
    for k,v in enumerate(lans):
        lans[k].append(url_cat(v[0]))
    ans = pd.DataFrame(lans)
    ans.to_csv('yrl_from.csv',index=False,header=None)


