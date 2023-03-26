# Import package
import wikipediaapi
import wiki_scrapper.filter as wikifilter
import re
import difflib
def main():
    textOriginal = wikifilter.read_text('C:/Users/Lemi/Documents/Spring 2023/CS3141 - Group Project/Software/TSP-7/src/wiki_scrapper/randomTextTest.txt');    # splits the text into an array of words
    finalText = filterOutCommonWords(textOriginal)
    print(finalText)

def filterOutCommonWords(textList):
    commonWords = 'C:/Users/Lemi/Documents/Spring 2023/CS3141 - Group Project/Software/TSP-7/src/wiki_scrapper/resources/commonwords.txt'
    commonList = wikifilter.read_text(commonWords)

    copyOfTextList = [ele for ele in textList]
    for x in textList:
        if x.lower() in commonList:
            copyOfTextList.remove(x)

    return copyOfTextList

if __name__ == "__main__":
    main()
        