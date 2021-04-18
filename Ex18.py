import math

import numpy as np

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''


def main(text):
    # tasks your code should perform:

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal
    # despite casing) can be done with
    docs = [line.lower().split() for line in text.split('\n')]
    uniques = (list(set(text.lower().split())))

    tf = dict()
    df = dict()

    for word in uniques:
        tf[word] = [line.count(word) / len(line) for line in docs]
        df[word] = sum([word in doc for doc in docs]) / len(docs)

    # 3. after you have your term frequencies and document frequencies, go over each line in the text and
    # calculate its TF-IDF representation, which will be a vector

    tfidf = []
    for line in range(len(docs)):
        toAdd = []
        for word in uniques:
            toAdd.append(tf[word][line] * math.log(1 / df[word], 10))
        tfidf.append(toAdd)

    N = len(tfidf)
    dist = np.empty((N, N), dtype=np.float)

    for i in tfidf:
        for j in tfidf:
            som = 0
            for item_i, item_j in zip(i, j):
                som += abs(item_i - item_j)
            if som == 0:
                som = np.inf
            dist[tfidf.index(i), tfidf.index(j)] = som
    print(np.unravel_index(np.argmin(dist), dist.shape))

    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.


main(text)
