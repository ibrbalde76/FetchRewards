#!/usr/bin/python
import math
import string
from read_file import *
import difflib
from sys import argv

# returns the words of each line
# into a list after transforming
# the lines into string
def words(lines):
    translation_table = str.maketrans(string.punctuation+string.ascii_uppercase,
                                     " "*len(string.punctuation)
                                     +string.ascii_lowercase)
    lines = lines.translate(translation_table)
    line_words = lines.split()

    return line_words

# count the occurrences of each word
def word_count(words):
    count = {}
    for word in words:
        if word in count:
            count[word] = count[word] + 1
        else:
            count[word] = 1
    return count

# return the word occurences of each
# word through a (word, occurrence)
# dictionary
def word_occurrences_dict(text):
    lines = read_file(text)
    line_words = words(lines)
    word_occurences = word_count(line_words)

    return word_occurences

# text similarity
# if text1 = text2 1
# if every_word(text1) != every_word(text2) 0
# else similarity_ratio(word_occurrences(text1),word_occurrences(text2))
def text_similarity(text1,text2):
    words1 = word_occurrences_dict(text1)
    words2 = word_occurrences_dict(text2)
    matching_words = difflib.SequenceMatcher(None,list(words1.keys()),list(words2.keys()))
    if (matching_words.ratio() <= 0.5):
        print("The texts are not similar")
    if (matching_words.ratio() > 0.5 and matching_words.ratio() < 1):
        print("The texts are very similar")
    else:
        print("The texts are identical")
    return matching_words.ratio()

text1 = sys.argv[1]
text2 = sys.argv[2]
print(text_similarity(text1,text2))
