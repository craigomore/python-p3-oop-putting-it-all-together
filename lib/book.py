
class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    # title property
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if type(value) is not str:
            raise TypeError("title must be a string")
        self._title = value

    # page_count property
    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if type(value) is not int:
            raise TypeError("page_count must be an integer")
        self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")



