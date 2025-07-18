# -*- coding: utf-8 -*-
"""tokenizer.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1upFY0ukPWB-twVpY9IluqmQt9uMT0bNr
"""

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
texts=[
    'I Like Python',
    'I Love Python',
    'Python programming',
]
tokenizer=Tokenizer()
tokenizer.fit_on_texts(texts)
sequence=tokenizer.texts_to_sequences(texts)
padding_post=pad_sequences(sequence,padding='post')
padding_pre=pad_sequences(sequence,padding='pre')
print("separated words with index ",tokenizer.word_index)
print("sequence are ",sequence)
print("The padding is ",padding)