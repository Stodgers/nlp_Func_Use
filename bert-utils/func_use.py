import math
import time
from extract_feature import BertVector
bv = BertVector()
nsd = bv.encode(['今天天气不错'])
print(nsd)
print(type(nsd),len(nsd[0]),nsd.shape)
# for i in range(10):
#     tt = input()
#     lis= [str(tt)]
#     #print(lis)
#     t1 = time.time()
#     sk = bv.encode(lis)
#     t2 = time.time()
#     print(int(round(t2 * 1000))-int(round(t1 * 1000))," ms")
print('-------------------')
while(1):
    tt1 = input()
    stt1= [str(tt1)]

    tt2 = input()
    stt2= [str(tt2)]
    t1 = time.time()
    sk1 = bv.encode(stt1)[0]
    sk2 = bv.encode(stt2)[0]
    fz = 0
    fm1 = 0
    fm2 = 0
    for i in range(len(sk1)):
        a = sk1[i]
        b = sk2[i]
        fz += a*b
        fm1 += a*a
        fm2 += b*b
    ans = fz/math.sqrt(fm1*fm2)
    t2 = time.time()
    print(int(round(t2 * 1000))-int(round(t1 * 1000))," ms")
    print(ans)


