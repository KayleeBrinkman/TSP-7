###################################
#    i don't even know what i'm   #
#    looking at here anymore      #
#    - andy                       #
###################################


import wikipediaapi
import re
import difflib

from page_getter import *


def related_pages(title: str, size: int) -> dict:
    print('running again')

    """
    obtains a list of x size of pages related to the original page

    :param title: original page to compare to
    :return: dictionary of pages related to the original search, sorted by similarity score
    """

    related_original: dict = {}
    final: dict = {}
    list_related = get_related(title)
    for x in list_related:
        xtitle = x[30:]     # gets title of article from link
        xscore = compare(title, xtitle)     # gets similarity score to original article
        add(related_original, xscore, xtitle)

    # adds key, value pairs to original list of sorted
    keys = list(related_original.keys())
    keys.sort(reverse=True)
    for i in keys:
        for j in related_original[i]:
            add(final, i, j)
    # TODO: find a way to make this run recursively until the list reaches x size
    # issue comes when, what if the list doesn't reach x size?
    # i don't even know anymore honestly

    return final


def add(dictionary: dict, key: int, value: str) -> dict:
    """
    adds an element to dictionary, sorts the dictionary by similarity score, then returns the dictionary
    :param dictionary: dict to add element to
    :param value: article name
    :param key: similarity score
    :return: sorted dictionary with new key,value pair
    """
    if key not in dictionary:
        dictionary[key] = list()
        dictionary[key].append(value)
    else:
        if value not in list(dictionary[key]):
            dictionary[key].append(value)

    return dictionary


def compare(a: str, b: str) -> int:

    """
    method based off of lemi's code in ScrappeAndCompare.py -- unsure if she has written a method for it yet as
    nothing is in github -- can be deleted later if she has, but i needed something for testing

    implements a percentage of similar words to calculate the score (so we have something standardized across all articles)
    score = number of matching words / word count of other article
    score is scaled from 1-100
    :param a: original article
    :param b: article to be compared to original
    :return: similarity score between the two articles
    """

    # calls page by page title
    wiki = wiki = wikipediaapi.Wikipedia('en')
    wiki1 = wiki.page(a)
    wiki2 = wiki.page(b)

    # exctract text from the page
    # original text
    text1 = wiki1.text
    text1 = re.sub(r'==.*?==+', '', text1)  # take any "" out
    text1 = text1.replace('\n', '')  # take out all \n
    textOriginal = text1.split(' ')  # splits the text into an array of words
    # other text to be considered
    text2 = wiki2.text
    text2 = re.sub(r'==.*?==+', '', text2)  # take any "" out
    text2 = text2.replace('\n', '')  # take out all \n
    textOther = text2.split(' ')  # splits the text into an array of words

    # compare the two texts, word by word
    matcher = difflib.SequenceMatcher(a=textOriginal, b=textOther)
    counter = 0
    for match in matcher.get_matching_blocks():
        counter = counter+1

    score = counter/len(textOther)*100      # score represents the percentage of words in article b that match article a
    return round(score, 2)


# unit testing/print debugging
print(compare('anime', 'Dragon Ball'))
print(compare('fruit', 'apple'))
testdict = {1: ['help'], 2: ['ugh'], 3: ['i\'m going to start sobbing']}
print(add(testdict, 1, 'please work for the love of god'))
print(add(testdict, 2, 'ugh'))
print(related_pages('apple', 50))


