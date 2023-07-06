# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 00:17:07 2023

@author: sena
"""

import os
import ast
import random
import keyword
import astunparse

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
        file_content = file.read()

    # Soy ağacı oluşturma
    tree = ast.parse(file_content)

    # Anahtar kelime veya sembol değiştirme işlemi
    transformer = KeywordReplacementTransformer()
    transformed_tree = transformer.visit(tree)

    # Dönüştürülen kodu yeniden oluşturma
    transformed_code = astunparse.unparse(transformed_tree)
    return transformed_code

class KeywordReplacementTransformer(ast.NodeTransformer):
    def __init__(self):
        self.keyword_replaced = False

    def visit_Name(self, node):
        # Anahtar kelimeyi rastgele bir hatalı versiyonla değiştirme
        if not self.keyword_replaced and isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load) and isinstance(node.id, str) and not node.id.startswith('__'):
            wrong_keyword = get_wrong_keyword(node.id)
            new_node = ast.Name(id=wrong_keyword, ctx=node.ctx)
            self.keyword_replaced = True
            return new_node
        return node

def get_wrong_keyword(keyword):
    # Hatalı versiyonlu anahtar kelimeleri veya sembolleri ekle
    wrong_keyword = keyword_replacement(keyword)
    return wrong_keyword

def write_transformed_code(file_path, transformed_code):
    with open(file_path, 'w') as file:
        file.write(transformed_code)

def keyword_replacement(keyword):
    replacements = {
        'print': 'prnt',
        'for': 'fr',
        'if': 'fi',
        'else': 'els',
        'while': 'whl',
        'break': 'brk',
        'continue': 'contnue',
        'def': 'df',
        'return': 'retrn',
        'import': 'imprt',
        'from': 'frm',
        'as': 's',
        'class': 'clss',
        'try': 'tryy',
        'except': 'exceptt',
        'finally': 'finaly',
        'raise': 'rase',
        'assert': 'assrt',
        'with': 'wit',
        'yield': 'yeld',
        'global': 'gloabl',
        'nonlocal': 'nonlcal',
        'del': 'dell',
        'lambda': 'lmbda',
        'and': 'adn',
        'or': 'orr',
        'not': 'ntt',
        'in': 'n',
        'is': 'iss',
        'True': 'Tre',
        'False': 'Flse',
        'None': 'Nne',
        'int': 'nt',
        'float': 'fot',
        'str': 'sr',
        'list': 'lit',
        'tuple': 'tple',
        'dict': 'dct',
        'set': 'st',
        'bool': 'bol',
        'len': 'lenght',
        'range': 'rng',
        'max': 'maax',
        'min': 'mn',
        'sum': 'sm',
        'abs': 'ab',
        'round': 'rund',
        'random': 'randm',
        'math': 'mt',
        'os': 'oss',
        'sys': 'sy',
        'datetime': 'dattime',
        'json': 'jsn',
        'pickle': 'pckle',
        'numpy': 'nmpy',
        'pandas': 'pndas'
    }

    if keyword in replacements:
        return replacements[keyword]
    return keyword

# Klasör yollarını
source_folder_path = 'VERISETI'
output_folder_path = 'VERISETI_YENI'

# Yeni ve yanlış dosyaların oluşturulması
create_wrong_files(source_folder_path, output_folder_path)
