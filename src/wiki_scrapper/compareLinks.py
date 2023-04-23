import wiki_scrapper.page_getter as pageGetter

def main():
    same_links = comapreLinks('anime', 'dragon ball')
    print('Same Links = \n')
    print(same_links)

def comapreLinks(title1, title2):
    links1 = set(pageGetter.get_links(title1))
    links2 = set(pageGetter.get_links(title2))

    return links1.intersection(links2)

if __name__ == "__main__":
    main()