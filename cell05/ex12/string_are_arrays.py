#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    count = sys.argv[1].count('z') # หาว่ามี z กี่ตัว
    if count == 0:
        print("none")
    else:
        print("z" * count)