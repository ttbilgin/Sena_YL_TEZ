# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 17:24:23 2023

@author: sena
"""

from sklearn.model_selection import train_test_split
import numpy as np
from numpy import array

def split_sequence(sequence, n_steps):
     X, y = list(), list()
     for i in range(len(sequence)):
     # find the end of this pattern
         end_ix = i + n_steps
         # check if we are beyond the sequence
         if end_ix > len(sequence)-1:
             break
     # gather input and output parts of the pattern
         seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
         X.append(seq_x)
         y.append(seq_y)
     return array(X), array(y);
 
# define input sequence
raw_seq = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# choose a number of time steps
n_steps = 3
# split into samples
X, y = split_sequence(raw_seq, n_steps)
# summarize the data
#for i in range(len(X)):
#    print(X[i], y[i])

####################################

with open('output_karisik.txt') as f:
    temp = [line.strip() for line in f.readlines()]

result = []
for word in temp:
    result.append(word.split(' '))
    #print(result)

flat_list = [item for sublist in result for item in sublist]
kelime = np.array(flat_list)
n_steps = 3
# split into samples
X, y = split_sequence(kelime, n_steps)

#for i in range(len(X)):
#    print(X[i], y[i])    

print(X.shape)
#(848, 3)

# reshape from [samples, timesteps] into [samples, timesteps, features]
n_features = 1
X = X.reshape((X.shape[0], X.shape[1],n_features))
X.shape
print(X.shape)
#(848, 3, 1)

X = X.astype(np.float)
y = y.astype(np.float)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.32, random_state = 0)


X_test.shape
print(X_test.shape)
#(111, 3)

# reshape from [samples, timesteps] into [samples, timesteps, features]
n_features = 1
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], n_features))
X_test.shape
print(X_test.shape)
#(111, 3, 1)

X_test = X_test.astype(np.float)
y_test = y_test.astype(np.float)

#########################

from numpy import array
from numpy import argmax
from keras.utils import to_categorical


y_train.shape
y_train = to_categorical(y_train)
y_train.shape
y_test.shape
y_test = to_categorical(y_test)
y_test.shape


import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.layers import Embedding, LSTM, Dense
from keras.models import Sequential
from keras.layers import TimeDistributed , Bidirectional, Input
from keras.utils import to_categorical
from keras.losses import categorical_crossentropy
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping
import pickle
import numpy as np
import os

no_classes = 157
callback = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=15)
# define model
model = Sequential()
model.add(LSTM(100, activation='relu',return_sequences=True, input_shape=(n_steps, n_features)))
model.add(LSTM(200, activation='relu', return_sequences=True))
model.add(LSTM(300, activation='relu' ,return_sequences=True))
model.add(LSTM(400, activation='relu', return_sequences=False))
#model.add(Bidirectional(LSTM(100, activation='relu',return_sequences=True), input_shape=(n_steps, n_features)))
#model.add(Bidirectional(LSTM(200, activation='relu', return_sequences=True)))
#model.add(Bidirectional(LSTM(300, activation='relu' ,return_sequences=True)))
#model.add(Bidirectional(LSTM(400, activation='relu', return_sequences=False)))
model.add(Dense(no_classes, activation='softmax'))
#model.compile(optimizer='adam', loss='mse')

model.compile(loss=categorical_crossentropy,
              optimizer='Adam',
              metrics=['accuracy'])
# fit model
model.summary()
history=model.fit(X_train, y_train,validation_data=(X_test, y_test),epochs=500,callbacks=[callback])
model.save('saved_model2/my_model2')

