#!/usr/bin/env python3
import sys

current_code = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    code, count = line.split('\t')
    count = int(count)
    
    if current_code == code:
        current_count += count
    else:
        if current_code:
            print(f"{current_code}\t{current_count}")
        current_code = code
        current_count = count

if current_code == code:
    print(f"{current_code}\t{current_count}")