# Import package
import wikipediaapi
import wiki_scrapper.filter as wikifilter
import wiki_scrapper.FilterOut as wikiFilterOut
import re
import difflib

def main():
    originalTitle = 'Anime'
    title = 'Dragon Ball'
    score = scrappe(originalTitle, title)
    print(score)

def scrappe(originalTitle, title):
    # CALLS THE PAGE BY PAGE TITLE
    wiki = wikipediaapi.Wikipedia('en')
    wiki1 = wiki.page('anime')
    wiki2 = wiki.page('dragon ball')

    # EXTRACT THE TEXT FROM THE WIKI PAGE
    # original text
    text1 = wiki1.text
    text1 = re.sub(r'==.*?==+', '', text1)  # take any "" out
    text1 = text1.replace('\n', '')         # take out all \n
    text1 = text1.split()   # creates a list
    textOriginal = wikiFilterOut.filterOutCommonWords(text1)  

    # other text to be considered
    text2 = wiki2.text
    text2 = re.sub(r'==.*?==+', '', text2)  # take any "" out
    text2 = text2.replace('\n', '')         # take out all \n
    text2 = text2.split()    # creates a list
    textOther = wikiFilterOut.filterOutCommonWords(text2)

    # COMPARE THE TWO TEXTS, WORD BY WORD
    score = 0
    for x in textOriginal:
        for y in textOther:
            if x == y:
                score = score+1
    otherTextSize = len(textOther)
    return (score/otherTextSize)

if __name__ == "__main__":
    main()
