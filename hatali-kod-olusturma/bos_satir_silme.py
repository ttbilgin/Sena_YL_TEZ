# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 00:19:09 2023

@author: sena
"""

import os

def remove_blank_lines_in_folder(folder_path):
    # Klasördeki dosyaları al
    file_paths = get_python_files(folder_path)

    # Dosyalardaki boş satırları sil
    for file_path in file_paths:
        remove_blank_lines(file_path)

def get_python_files(folder_path):
    python_files = []
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(".py"):
                file_path = os.path.join(root, file_name)
                python_files.append(file_path)
    return python_files

def remove_blank_lines(file_path):
    # Dosyayı oku
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Boş satırları filtrele
    non_blank_lines = [line for line in lines if line.strip()]

    # Dosyayı tekrar yaz
    with open(file_path, 'w') as file:
        file.writelines(non_blank_lines)

# Kullanım örneği
folder_path = 'VERISETI_YENI'  # Boş satırların silineceği klasörün yolu
remove_blank_lines_in_folder(folder_path)
