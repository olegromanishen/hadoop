#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    code, count, category = line.split('\t')
    count = int(count)
    print(f"{count}\t{code}\t{category}")