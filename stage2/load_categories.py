import os

def load_categories(directory):
    categories = {}
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r', encoding='cp866') as f:
                for line in f:
                    parts = line.strip().split('|')
                    code_prefix = parts[0]
                    category = parts[1]
                    # Используем последнюю актуальную запись для каждой категории
                    if code_prefix not in categories or len(parts[4]) == 0:
                        categories[code_prefix] = category
    return categories