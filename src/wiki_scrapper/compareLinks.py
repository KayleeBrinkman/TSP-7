import src.wiki_scrapper.page_getter as pageGetter

def main():
    same_links = comapreLinks('anime', 'dragon ball')
    print('Same Links = \n')
    print(same_links)

def comapreLinks(title1, title2):
    links1 = pageGetter.get_links(title1)
    links2 = pageGetter.get_links(title2)

    sameLinks = set()
    for x in links1:
        for y in links2:
            if x == y:
                sameLinks.add(x)
    return sameLinks

if __name__ == "__main__":
    main()