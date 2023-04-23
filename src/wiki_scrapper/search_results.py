import wikipediaapi
import re
import difflib
import os

from wiki_scrapper.result import Result
from wiki_scrapper.page_getter import *
from wiki_scrapper.ScrappeAndCompare import *



def related_pages(title: str, count=None) -> list:
    """
    Obtains a sorted list of pages related to the original page
    :param title: original page to compare to
    :return: List of pages related to the original search, sorted by similarity score
    """

    mainWiki = Result()
    mainWiki.set_title(title)
    storeTest = f'{os.path.dirname(__file__)}\\resources\\storetest.txt'
    prevSearch = mainWiki.check_title(storeTest, mainWiki.get_title())
    if 'dict_items' in prevSearch:
        prevRelated = []
        r = re.compile("[^)]*")
        m = r.findall(prevSearch)
        print(m)
        prevRelated = m
        prevRelated.sort(key=lambda x: x[1], reverse=True)
        return prevRelated
    info = get_info(title)
    related = []
    for related_page in info['related']:
        related_info = get_info(related_page)
        related_title = related_info['title']
        score = scrappe(title, related_title)
        related.append((related_title, score))
    # Sort by similarity score
    related.sort(key = lambda x: x[1], reverse=True)
    if count:
        related = related[:count]
    tempDict = {}
    for page in related:
        tempDict[page[0]] = page[1]
    mainWiki.set_articles(tempDict)
    mainWiki.store_result(storeTest)

    return related


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
        counter += 1

    score = counter / len(textOther) * 100      # score represents the percentage of words in article b that match article a
    return round(score, 2)

if __name__ == "__main__":
    # unit testing/print debugging
    print(compare('anime', 'Dragon Ball'))
    print(compare('fruit', 'apple'))
    print(related_pages('apple', 10))