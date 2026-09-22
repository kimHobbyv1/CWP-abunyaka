#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 3: #sys.argv[1] คำที่ต้องการค้นหา, sys.argv[2] เป็นข้อความที่ใช้ค้นหา
    print("none")
else:
    matches = re.findall(sys.argv[1], sys.argv[2])
    if len(matches) == 0:
        print("none")
    else:
        print(len(matches))