import random
import pickle
import numpy as np
import pandas as pd
from nltk.tokenize import RegexpTokenizer

import tensorflow
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dense, Activation
from keras.optimizers import RMSprop
import keras.layers
import keras.models
text_data = pd.read_csv("Backend\\Features\\fake_or_real_news.csv")
text = list(text_data.text.values)
joined_text = " ".join(text)
partial_text = joined_text[:300000]

tokenizer = RegexpTokenizer(r"\w+")
tokens = tokenizer.tokenize(partial_text.lower())

unique_tokens = list(np.unique(tokens))
unique_tokens_index = {token: idx for idx, token in enumerate(unique_tokens)}

in_words = 10
'''
input_words = []
next_words = []


for i in range(len(tokens) - in_words):
    input_words.append(tokens[i:i + in_words])
    next_words.append(tokens[i + in_words])

X = np.zeros((len(input_words), in_words, len(unique_tokens)), dtype=bool)
Y = np.zeros((len(next_words), len(unique_tokens)), dtype=bool)

for i, words in enumerate(input_words):
    for j, word in enumerate(words):
        X[i, j, unique_tokens_index[word]] = 1
    Y[i, unique_tokens_index[next_words[i]]] = 1

model = Sequential()
model.add(LSTM(128, input_shape=(in_words, len(
    unique_tokens)), return_sequences=True))
model.add(LSTM(128))
model.add(Dense(len(unique_tokens)))
model.add(Activation("softmax"))

model.compile(loss="categorical_crossentropy", optimizer=RMSprop(
    learning_rate=0.01), metrics=["accuracy"])
model.fit(X, Y, batch_size=128, epochs=30, shuffle=True)
model.save("generatortext.keras")

'''
model = load_model("generatortext.keras")


def predict_next_word(input_text, n_best):
    input_text = str(input_text).lower()
    X = np.zeros((1, in_words, len(unique_tokens)))
    for i, word in enumerate(input_text.split()):
        X[0, i, unique_tokens_index[word]] = 1

    predictions = model.predict(X)[0]
    return np.argpartition(predictions, -n_best)[-n_best:]


def generate_text(input_text, text_length, creativity=3):
    word_sequence = str(input_text).split()
    current = 0
    for _ in range(text_length):
        sub_sequence = " ".join(tokenizer.tokenize(
            " ".join(word_sequence).lower())[current:current+in_words])
        try:
            choice = unique_tokens[random.choice(
                predict_next_word(sub_sequence, creativity))]
        except:
            choice = random.choice(unique_tokens)

        word_sequence.append(choice)
        current += 1
    return " ".join(word_sequence)


generated_text = generate_text("She said to me ", 20, 5)
print(generated_text)
