#!/usr/bin/env python3
import sys
from load_categories import load_categories

# Считываем справочник категорий
categories = load_categories('tnved')

for line in sys.stdin:
    line = line.strip()
    code, count = line.split('\t')
    category = categories.get(code, 'ПРОЧЕЕ')
    print(f"{code}\t{count}\t{category}")