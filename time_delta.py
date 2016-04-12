# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 +0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 +0000

import calendar
from datetime import datetime

t = int(input())

for test_case in range(t):
    j1 = input().split()
    j2 = input().split()

    s1 = j1[0]+":"+j1[1]+":"+j1[2]+":"+j1[3]+":"+j1[4]+":"+j1[5]
    s2 = j2[0]+":"+j2[1]+":"+j2[2]+":"+j2[3]+":"+j2[4]+":"+j2[5]
    print(s1, s2)
    FMT = '%a:%d:%b:%Y:%H:%M:%S:%z'
    tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
    print (int(abs(tdelta.total_seconds())))
