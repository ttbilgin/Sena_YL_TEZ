# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 21:59:52 2023

@author: sena
"""

import os
import ast

def find_files_with_syntax_errors(folder_path):
    files_with_errors = []

    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(".py"):
                file_path = os.path.join(root, file_name)
                if has_syntax_errors(file_path):
                    files_with_errors.append(file_path)

    return files_with_errors

def has_syntax_errors(file_path):
    with open(file_path, 'r') as file:
        try:
            ast.parse(file.read())
        except SyntaxError:
            return True
    return False

# Klasör yolunu belirtin
folder_path = 'VERISETI'

# Hatalı sözdizimine sahip dosyaları bul
files_with_errors = find_files_with_syntax_errors(folder_path)

# Hatalı dosyaları yazdır
for file_path in files_with_errors:
    print(file_path)
