import os
import random
import keyword

def create_wrong_files(source_folder_path, output_folder_path):
    file_paths = get_python_files(source_folder_path)
    if len(file_paths) == 0:
        print("Hata: Kaynak klasörde Python dosyası bulunamadı.")
        return

    for file_path in file_paths:
        transformed_code = create_wrong_version(file_path)

        file_name = os.path.basename(file_path)
        new_file_path = os.path.join(output_folder_path, file_name)
        write_transformed_code(new_file_path, transformed_code)

def get_python_files(folder_path):
    python_files = []
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(".py"):
                file_path = os.path.join(root, file_name)
                python_files.append(file_path)
    return python_files

def create_wrong_version(file_path):
    with open(file_path, 'r') as file:
        file_content = file.readlines()

    transformed_code = []
    for line in file_content:
        transformed_line = line.strip()
        if transformed_line:
            transformed_code.append(transformed_line)

    random_line_index = random.randint(0, len(transformed_code))
    random_keyword = get_random_keyword()
    transformed_code.insert(random_line_index, random_keyword)

    return "\n".join(transformed_code)

def get_random_keyword():
    keywords_and_symbols = keyword.kwlist + ['+', '-', '*', '/', '=', '==', '!=', '<', '>', '<=', '>=', 'and', 'or', 'not', 'is', 'in']
    return random.choice(keywords_and_symbols)

def write_transformed_code(file_path, transformed_code):
    with open(file_path, 'w') as file:
        file.write(transformed_code)

# Klasör yolları
source_folder_path = 'VERISETI'  # Doğru yazılmış Python dosyalarının bulunduğu klasörün yolu
output_folder_path = 'VERISETI'  # Yanlış dosyaların oluşturulacağı klasörün yolu

# Yeni ve yanlış dosyaların oluşturulması
create_wrong_files(source_folder_path, output_folder_path)
