# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 13:13:47 2023

@author: sena
"""

#HATANIN SATIR VE SUTUN CINSINDEN KONUMUNUN BULUNMASI

import ast

def check_syntax(code):
    try:
        ast.parse(code)
        print("Syntax is valid.")
        return None  # Hata yok, None döndürülüyor
    except SyntaxError as e:
        line_number = e.lineno
        column_offset = e.offset
        error_message = e.msg
        print("Syntax error at line {}, column {}: {}".format(line_number, column_offset, error_message))
        return line_number, column_offset, error_message

# Örnek kullanım
dosya='hatalikod5.py'
with open(dosya, "r") as file:
    code = file.read()

result = check_syntax(code)
if result is not None:
    
    # Değerleri kullanarak değişkenlere atama
    line_number, column_offset, error_message = result
    print(line_number, column_offset,error_message)
    
