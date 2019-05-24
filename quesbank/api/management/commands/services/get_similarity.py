import math
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from bs4 import BeautifulSoup as BS

import json
import os


def get_similarity(Q, questions, qids):
    # ind = questions.index(Q)
    # questions = questions[:ind] + questions[ind+1:]
    # qids = qids[:ind] + qids[ind+1:]
    questions = [to_str(ques) for ques in questions]
    vect = TfidfVectorizer()
    tfidf = vect.fit_transform(questions)
    Q = to_str(Q)
    self_vect = vect.transform([Q])[0]
    cossim = linear_kernel(self_vect, tfidf)
    return cossim[0], qids


def to_str(string):
    string = get_ques(string)
    string = remove_stop_words(string)
    return string.strip().lower()


def remove_stop_words(ques):
    check_packages()

    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(ques)
    filtered = [w for w in word_tokens if not w in stop_words]
    ques = ' '.join(filtered)
    return ques


def get_ques(ques_html):
    obj = BS(ques_html, features='html.parser')
    return obj.getText()

import contextlib
import sys
@contextlib.contextmanager
def redirect_stdout(target):
    original = sys.stdout
    sys.stdout = target
    yield
    sys.stdout = original

def check_packages():
    try:
        nltk.data.find('tokenizers/punkt.zip')
    except LookupError:
        with redirect_stdout(open(os.devnull, "w")):
            nltk.download('punkt')
    try:
        nltk.data.find('corpora/stopwords.zip')
    except LookupError:
        with redirect_stdout(open(os.devnull, "w")):
            nltk.download('stopwords')


# Driver function to check
def get_sim_matrix(jsonObj):
    questions = []
    qids = []
    for x in jsonObj['data']:
        questions.append(x['question_html'])
        qids.append(x['id'])

    sim_matrix = []
    total_matrix = []
    for x in range(len(questions) - 1):
        sim, ids = get_similarity(questions[x], questions[x + 1:], qids[x + 1:])
        L = []
        for i in range(len(sim)):
            L.append((ids[i], math.ceil(sim[i]*100)))
        L.sort(key=lambda elem: elem[1], reverse=True)
        total_matrix.append(L)
        end = len(L)
        for i in range(len(L)):
            if L[i][1] < 80:
                end = i
                break
        if end == 0:
            continue
        else:
            L = L[:end]
        sim_matrix.append((qids[x], L))

    return sim_matrix
