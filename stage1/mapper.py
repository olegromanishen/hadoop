#!/usr/bin/env python3
import sys
import csv

for line in sys.stdin:
    line = line.strip()
    parts = list(csv.reader([line]))[0]
    # Получаем категорию из первых двух цифр кода
    category_code = parts[3][:2]
    print(f"{category_code}\t1")