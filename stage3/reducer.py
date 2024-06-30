#!/usr/bin/env python3
import sys

results = []

for line in sys.stdin:
    line = line.strip()
    count, code, category = line.split('\t')
    count = int(count)
    results.append((count, code, category))

# Сортировка по количеству записей в порядке убывания
results.sort(reverse=True, key=lambda x: x[0])

for count, code, category in results:
    print(f"{code}\t{count}\t{category}")