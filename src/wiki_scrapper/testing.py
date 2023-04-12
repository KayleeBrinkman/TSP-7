# testing for each individual method compiled into one file
# author: andrew anderson
# last updated 4/9/2023
from wiki_scrapper.compareLinks import *
from wiki_scrapper.filter import *
from wiki_scrapper.page_getter import *
from wiki_scrapper.ScrappeAndCompare import *
from wiki_scrapper.search_results import *


def main():
    ##################################
    # PAGE_GETTER.PY TESTS           #
    # TESTED WITH WIKI PAGE 'apple'  #
    ##################################

    # get_summary -> params (str)
    print('Testing get_summary method from page_getter.py . . .')
    print('Printing results for page \'apple\':')
    print(get_summary('apple'))
    print('\n')

    # get_photos -> params (str)
    print('Testing get_photos method from page_getter.py . . .')
    print('Printing results for page \'apple\':')
    print(get_photos('apple'))
    print('\n')

    # get_links -> params (str)
    print('Testing get_links method from page_getter.py . . .')
    print('Printing results for page \'apple\':')
    print(get_links('apple'))
    print('\n')

    # get_related -> params (str)
    print('Testing get_related method from page_getter.py . . .')
    print('Printing results for page \'apple\':')
    print(get_related('apple'))
    print('\n')

    # get_info -> params (str)
    print('Testing get_info method from page_getter.py . . .')
    print('Printing results for page \'apple\':')
    print(get_info('apple'))
    print('\n')

    ##################################
    # SCRAPPEANDCOMPARE.PY TESTS     #
    # TESTED WITH WIKI PAGE 'apple'  #
    # AND WIKI PAGE 'orange'         #
    ##################################

    # scrappe -> params (str, str)
    print('Testing scrappe method from ScrappeAndCompare.py . . .')
    print('Printing results for comparing page \'orange\' to \'apple\': ')
    print('Percentage of similar words (excluding common words): ', scrappe('apple', 'orange'))
    print('\n')

    ##################################
    # COMPARELINKS.PY TESTS          #
    # TESTED WITH WIKI PAGE 'apple'  #
    # AND WIKI PAGE 'orange'         #
    ##################################

    # compareLinks -> params (str, str)
    print('Testing compareLinks method from compareLinks.py . . .')
    print('Links from page \'apple\': ')
    print(get_links('apple'))
    print('Links from page \'orange\': ')
    print(get_links('orange'))
    print("Links shared between the two pages: ")
    sameLinks = comapreLinks('apple', 'orange')
    sharedLinks = []
    for x in sameLinks:
        sharedLinks.append(x)
    print(sharedLinks)
    print('\n')

    ##################################
    # COMPARELINKS.PY TESTS          #
    # TESTED WITH WIKI PAGE 'apple'  #
    # AND WIKI PAGE 'orange'         #
    ##################################

    # compareLinks -> params (str, str)
    print('Testing compareLinks method from compareLinks.py . . .')
    print('Links from page \'apple\': ')
    print(get_links('apple'))
    print("Links shared between the apple and itself: ")
    sameLinks = comapreLinks('apple', 'apple')
    sharedLinks = []
    for x in sameLinks:
        sharedLinks.append(x)
    print(sharedLinks)
    print('\n')

    ##################################
    # FILTER.PY TESTS                #
    # TESTED WITH MANUAL LISTS       #
    ##################################
    print('Testing filter_words method from filter.py . . .')
    listOfWords = ['MTU', 'Huskies', 'and', 'a', 'CS3141', 'the']
    print('Removing common words from ', listOfWords)
    listOfWords = filter_words(listOfWords)
    print('Filtered list: ', listOfWords)
    print('\n')

    ##################################
    # SEARCH_RESULTS.PY TESTS        #
    # TESTED WITH WIKI PAGE 'apple'  #
    ##################################
    print('Testing search_results method from search_results.py . . .')
    print('Pages related to wiki page \'apple\'')
    print(related_pages('apple', None))



if __name__ == "__main__":
    main()
