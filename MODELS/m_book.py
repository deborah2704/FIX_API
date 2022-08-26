import datetime
from MODELS.m_basicObj import BasicObj


class Book(BasicObj):
    def __init__(self, cc: str, title: str, t_title: str, author: str, date: datetime, publishing: str, num_of_page: int, descript_book: str, web_site: str):
        self._cc = None
        self._title = None
        self._t_title = None
        self._author = None
        self._publish_date = None
        self._publisher = None
        self._pages = None
        self._description = None
        self._website = None

        if not isinstance(cc, str):
            raise TypeError("the book must to be a string!")
        self._cc = cc

        if not isinstance(title, str):
            raise TypeError("the book title must to be a string!")
        self._title = title

        if not isinstance(t_title, str):
            raise TypeError("the subtitle of book must to be a string!")
        self._sum_title = t_title

        if not isinstance(author, str):
            raise TypeError("the author of book must to be a string be a string!")
        self._author = author

        if not isinstance(date, datetime.datetime):
            raise TypeError("the publish date of book must be a Date!")
        self._publish_date = date

        if not isinstance(publishing, str):
            raise TypeError("the book publisher must be a string!")
        self._publisher = publishing

        if not isinstance(num_of_page, int):
            raise TypeError("the pages of book must be a number (int) !")
        self._pages = num_of_page

        if not isinstance(descript_book, str):
            raise TypeError("the description of book must be a string!")
        self._description = descript_book

        if not isinstance(web_site, str):
            raise TypeError("the website of book must be a string (link) !")
        self._website = web_site
