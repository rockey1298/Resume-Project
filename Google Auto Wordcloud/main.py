import string
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys


import os

cwd = os.path.dirname(__file__)
file_path = os.path.join(cwd, "beemoviescript.txt")
try:
    with open(file_path, "r") as f:
        file_contents = f.read()
    print(file_contents)
except:
    print("file not found.")


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = """!()-[]{};:'"\,<>./?@#$%^&*_~"""
    uninteresting_words = [
        "the",
        "a",
        "to",
        "if",
        "is",
        "it",
        "of",
        "and",
        "or",
        "an",
        "as",
        "i",
        "me",
        "my",
        "we",
        "our",
        "ours",
        "you",
        "your",
        "yours",
        "he",
        "she",
        "him",
        "his",
        "her",
        "hers",
        "its",
        "they",
        "them",
        "their",
        "what",
        "which",
        "who",
        "whom",
        "this",
        "that",
        "am",
        "are",
        "was",
        "were",
        "be",
        "been",
        "being",
        "have",
        "has",
        "had",
        "do",
        "does",
        "did",
        "but",
        "at",
        "by",
        "with",
        "from",
        "here",
        "when",
        "where",
        "how",
        "all",
        "any",
        "both",
        "each",
        "few",
        "more",
        "some",
        "such",
        "no",
        "nor",
        "too",
        "very",
        "can",
        "will",
        "just",
    ]

    # LEARNER CODE START HERE
    mydict = {}
    for line in file_contents.split("\n"):
        for word in line.split(" "):
            word = word.translate(str.maketrans("", "", string.punctuation))
            if word not in uninteresting_words:
                if word in mydict:
                    mydict[word] += 1
                else:
                    mydict[word] = 1

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(mydict)
    return cloud.to_array()


myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation="nearest")
plt.axis("off")
plt.show()
