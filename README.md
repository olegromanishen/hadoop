# MapReduce Pipeline for Categorizing Product Codes

## Общие шаги:
1. Скопируйте файлы кодов для каждой стадии на HDFS.
2. Выполните команды из командной строки Hadoop для каждой стадии, указав нужный путь к файлам

## Запуск стадии 1:

hadoop jar /path/to/hadoop-streaming.jar \
    -input /path/to/input.csv \
    -output /path/to/output/stage1 \
    -mapper stage1/mapper.py \
    -reducer stage1/reducer.py \
    -file stage1/mapper.py \
    -file stage1/reducer.py


## Запуск стадии 2:

hadoop jar /path/to/hadoop-streaming.jar \
    -input /path/to/output/stage1 \
    -output /path/to/output/stage2 \
    -mapper stage2/mapper.py \
    -reducer stage2/reducer.py \
    -file stage2/mapper.py \
    -file stage2/reducer.py \
    -file stage2/load_categories.py \
    -file -r stage2/tnved/

## Запуск стадии 3:

hadoop jar /path/to/hadoop-streaming.jar \
    -input /path/to/output/stage2 \
    -output /path/to/final_output \
    -mapper stage3/mapper.py \
    -reducer stage3/reducer.py \
    -file stage3/mapper.py \
    -file stage3/reducer.py