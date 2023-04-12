# Import package
import wikipediaapi
import wiki_scrapper.filter as wikifilter
import re
import difflib
def main():
    textOriginal = wikifilter.read_text('C:\\Users\\Caleb\\Desktop\\Python Programs\\TSP-7\\src\\wiki_scrapper\\commonwords.txt');    # splits the text into an array of words
    finalText = filterOutCommonWords(textOriginal)
    print(finalText)

def filterOutCommonWords(textList):
    commonWords = 'C:\\Users\\Caleb\\Desktop\\Python Programs\\TSP-7\\src\\wiki_scrapper\\resources\\commonwords.txt'
    commonList = wikifilter.read_text(commonWords)

    copyOfTextList = [ele for ele in textList]
    for x in textList:
        if x.lower() in commonList:
            copyOfTextList.remove(x)

    return copyOfTextList

if __name__ == "__main__":
    main()
        
