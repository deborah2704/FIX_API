from MODELS.m_basicObj import BasicObj


class Collection(BasicObj):
    def __init__(self, isbn: str):
        self._isbn = None

        if isbn is not None:
            if not isinstance(isbn, str):
                raise TypeError("isbn must be string")
            self._isbn = isbn

