# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 21:34:13 2023

@author: sena
"""

import os
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.optimizers import Adam



# Veri klasörlerinin yolu
folder_paths = ["DOGRU_VERISETI/","HATALI_DEGISMESI_GEREKENLER/", "HATALI_EKLENMIS_SILINMESI_GEREKIYOR/", "HATALI_SILINMIS_EKLENMESI_GEREKIYOR/"]

# Tüm metinlerin ve etiketlerin saklanacağı listeler
texts = []
labels = []

# Verilerin okunması
for folder_path in folder_paths:
    folder_label = folder_paths.index(folder_path)
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            texts.append(text)
            labels.append(folder_label)

# Metinlerin vektörlere dönüştürülmesi
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

# Metinlerin eşit boyutta hale getirilmesi (padding)
max_sequence_length = max([len(seq) for seq in sequences])
padded_sequences = pad_sequences(sequences, maxlen=max_sequence_length)

# Sınıf etiketlerinin numpy dizisine dönüştürülmesi
labels = np.array(labels)

# Modelin oluşturulması
model = Sequential()
model.add(Embedding(len(tokenizer.word_index) + 1, 16, input_length=max_sequence_length))
model.add(LSTM(100, activation='relu',return_sequences=True))
model.add(LSTM(200, activation='relu', return_sequences=True))
model.add(LSTM(300, activation='relu' ,return_sequences=True))
model.add(LSTM(400, activation='relu', return_sequences=False))
model.add(Dense(len(folder_paths), activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy', optimizer=Adam(lr=0.001), metrics=['accuracy'])
history=model.fit(padded_sequences, labels, epochs=500, batch_size=16)
model.save('saved_model_tur/hata_turu_model')

# Test veri klasörü
test_folder_path = "test_klasoru/"

# Test verilerinin okunması
test_texts = []
test_labels = []
for filename in os.listdir(test_folder_path):
    file_path = os.path.join(test_folder_path, filename)
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        test_texts.append(text)

# Test metinlerinin vektörlere dönüştürülmesi ve padding
test_sequences = tokenizer.texts_to_sequences(test_texts)
padded_test_sequences = pad_sequences(test_sequences, maxlen=max_sequence_length)

# Tahminlerin alınması
predictions = model.predict(padded_test_sequences)
predicted_labels = np.argmax(predictions, axis=1)

# Tahminlerin yazdırılması
for i, text in enumerate(test_texts):
    print(f"Metin: {text} - Tahmin: {folder_paths[predicted_labels[i]]}")
