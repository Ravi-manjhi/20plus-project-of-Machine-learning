import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


class FakeNews:

    def clean_msg(self, text):
        words = []
        stemmer = PorterStemmer()
        word = word_tokenize(text)
        stopword = set(stopwords.words('english'))
        for w in word:
            w = w.lower()
            if w.isalpha():
                if w not in stopword:
                    text = stemmer.stem(w)
                    words.append(text)

        return ' '.join(words)

    def fake_news_detection(self, clean_function, text):
        words = self.clean_msg(text)
