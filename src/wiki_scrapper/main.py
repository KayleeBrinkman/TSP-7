# This is a sample Python script
from result import Result
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    title = "test title"
    articles = { "apple":10, "orange":20, "banana":5 }
    test = Result(title, articles)
    print(test)
    test = test.sort_articles()
    print(test)

