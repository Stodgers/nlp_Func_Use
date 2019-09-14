import time
from extract_feature import BertVector
bv = BertVector()
print(bv.encode(['今天天气不错']))
for i in range(10):
    tt = input()
    lis= [str(tt)]
    #print(lis)
    t1 = time.time()
    sk = bv.encode(lis)
    t2 = time.time()
    print(int(round(t2 * 1000))-int(round(t1 * 1000))," ms")