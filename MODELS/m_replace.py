from MODELS.m_basicObj import BasicObj


class Replace(BasicObj):
    def __init__(self, user_id: str, isbn: str):
        self._userId = None
        self._isbn = None

        if user_id is not None:
            if not isinstance(user_id, str):
                raise TypeError("user id must be string")
            self._userId = user_id

        if isbn is not None:
            if not isinstance(isbn, str):
                raise TypeError("isbn must be string")
            self._isbn = isbn

    @property
    def isbn(self):
        return self._isbn


if __name__ == "__main__":
    C = Replace("sadoun", "isbn")
    print(C)
