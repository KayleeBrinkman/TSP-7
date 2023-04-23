# Import package
import wikipediaapi
import wiki_scrapper.filter as wikifilter
import wiki_scrapper.FilterOut as wikiFilterOut
import wiki_scrapper.compareLinks as wikiSameLinks
import re
import difflib
import result

def main():
    originalTitle = 'Anime'
    title = 'Dragon Ball'
    score = scrappe(originalTitle, title)
    print(score)

def scrappe(originalTitle, title):
    # CALLS THE PAGE BY PAGE TITLE
    wiki = wikipediaapi.Wikipedia('en')
    wiki1 = wiki.page(originalTitle)
    wiki2 = wiki.page(title)


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
    matcher = difflib.SequenceMatcher(a=textOriginal, b=textOther)
    score = matcher.real_quick_ratio()
    # counter = 0
    # for match in matcher.get_matching_blocks():
    #     counter = counter+1

    # score = counter/len(textOther)*100      # score represents the percentage of words in article b that match article a
    
    titleOgList = originalTitle.split()
    titleList = title.split()
    matcherTitle = difflib.SequenceMatcher(a=titleOgList, b=titleList)
    score *= matcherTitle.real_quick_ratio() + 1
    
    sameLinks = wikiSameLinks.comapreLinks(originalTitle, title)
    score = score*(1+len(sameLinks)*0.02)

    return round(score, 2)

if __name__ == "__main__":
    main()
