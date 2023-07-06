import os
import random
import keyword

def remove_random_token(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Dosyanın her bir satırını dolaşarak rastgele bir anahtar kelime veya sembolü bulma
    for i, line in enumerate(lines):
        tokens = line.split()

        # İlk 4 anahtar kelime veya sembolü atlayarak rastgele bir anahtar kelime veya sembolü bulma
        if len(tokens) > 4:
            tokens = tokens[4:]

            # Rastgele bir anahtar kelime veya sembolü seçme
            token_to_remove = random.choice(tokens)

            # Anahtar kelime veya sembolün dosyadaki ilk konumunu bulma
            token_start_index = line.find(token_to_remove)
            if token_start_index != -1:
                token_end_index = token_start_index + len(token_to_remove)

                # Anahtar kelime veya sembolü satırdan kaldırma
                updated_line = line[:token_start_index] + line[token_end_index:]
                lines[i] = updated_line
                break

    # Dosyanın üzerine yazma
    with open(file_path, 'w') as file:
        file.writelines(lines)

folder_path = 'VERISETI'  # Python dosyalarının bulunduğu klasörün yolu

# Klasördeki tüm Python dosyaları üzerinde işlem yapma
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            remove_random_token(file_path)
