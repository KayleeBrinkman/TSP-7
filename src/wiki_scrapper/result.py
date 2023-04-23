
class Result:

    def __init__(self, title=None, articles=None):
        self.searched_title = title
        self.related_articles = articles

    def __str__(self):
        return f"{self.searched_title}\n{self.related_articles.items()}"

    def sort_articles(self):
        sorted_articles = sorted(self.related_articles.items(), key = lambda x:x[1])
        return sorted_articles

    def get_title(self):
        return self.searched_title

    def get_articles(self):
        return self.related_articles

    def set_title(self, new_string):
        self.searched_title = new_string

    def set_articles(self, articles):
        self.related_articles = articles

    def add_article(self, title, score):
        self.related_articles[title] = score

    def change_score(self, title, score):
        self.related_articles[title] = score

    def store_result(self, file_path):
        with open (file_path, 'a') as f:
            f.write("\n" + (self.__str__()) + "\n")
    def check_title(self, file_path, title) -> str:
        with open(file_path, 'r') as f:
            found = False
            for line in f:
                if found:
                    return line
                if line.strip() == title:
                    found = True
                    continue
            if(not found):
                return "Not found"
            else:
                return "error"

