from result import Result
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    title = "test title"
    articles = { "apple":10, "orange":20, "banana":5 }
    test = Result(title, articles)
    print(test)
    print(test.sort_articles())
    test.store_result('storetest.txt')
    test.store_result('storetest.txt')


