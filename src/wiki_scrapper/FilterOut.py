# Import package
import wikipediaapi
import wiki_scrapper.filter as wikifilter
import re
import difflib
def main():
    textOriginal = wikifilter.read_text('wiki_scrapper\\randomTextTest.txt');    # splits the text into an array of words
    finalText = filterOutCommonWords(textOriginal)
    print(finalText)

def filterOutCommonWords(textList):
    commonWords = 'wiki_scrapper\\resource\\commonwords.txt'
    commonList = wikifilter.read_text(commonWords)

    copyOfTextList = [ele for ele in textList]
    for x in textList:
        if x.lower() in commonList:
            copyOfTextList.remove(x)

    return copyOfTextList

if __name__ == "__main__":
    main()
        
