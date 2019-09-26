import re
from itertools import groupby
def email_extracor(text):
    if text=='':
        return []
    filtrate = re.compile(u'[\u4E00-\u9FA5]')
    eng_texts = filtrate.sub(r' ', text)
    eng_texts = eng_texts.replace(' at ','@').replace(' dot ','.')
    sep = ',!?:; ，。！？《》、|\\/'
    #print('/'.join(eng_texts))
    eng_split_texts = [''.join(g) for k, g in groupby(eng_texts, sep.__contains__) if not k]
    # for k, g in groupby(eng_texts, sep.__contains__):
    #     print(k,''.join(g))
    email_pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z_-]+)+$'

    emails = []
    for eng_text in eng_split_texts:
        result = re.match(email_pattern, eng_text, flags=0)
        if result:
            emails.append(result.string)
    return emails
print(email_extracor('我的邮箱是123@2333.com，老李的邮箱是3@3.xyz、jjj@k.com并且我的老邮箱是kkiuhiuhiuh@c.on'))