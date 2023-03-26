# Import package
import wikipediaapi
import wiki_scrapper.filter as wikifilter
import wiki_scrapper.FilterOut as wikiFilterOut
import re
import difflib

def scrappe(originalTitle, title):
    # CALLS THE PAGE BY PAGE TITLE
    wiki = wikipediaapi.Wikipedia('en')
    wiki1 = wiki.page(originalTitle)       
    wiki2 = wiki.page(title)

    # EXTRACT THE TEXT FROM THE WIKI PAGE
    # original text
    text1 = wiki1.text;
    text1 = re.sub(r'==.*?==+', '', text1)  # take any "" out
    text1 = text1.replace('\n', '')         # take out all \n
    text1 = wikifilter.read_text(text1)     # creates a list
    textOriginal = wikiFilterOut.filterOutCommonWords(text1)  

    # other text to be considered
    text2 = wiki2.text;
    text2 = re.sub(r'==.*?==+', '', text2)  # take any "" out
    text2 = text2.replace('\n', '')         # take out all \n
    text2 = wikifilter.read_text(text2)     # creates a list
    textOriginal = wikiFilterOut.filterOutCommonWords(text2)

    # COMPARE THE TWO TEXTS, WORD BY WORD
    matcher = difflib.SequenceMatcher(a=textOriginal, b=textOther)
    print("\nMatching Sequences:")
    score = 0;
    for match in matcher.get_matching_blocks():
        score = score+1;
        print("Match             : {}\n".format(match))
        print("Matching Sequence : {}\n".format(textOriginal[match.a:match.a+match.size]))
    print("There are {} matching phrases or words\n".format(score))
    return score

