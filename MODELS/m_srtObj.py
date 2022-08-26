from MODELS.m_basicObj import BasicObj


class StringObject(BasicObj):
    def __init__(self, cc: str, user_id: str):
        self._cc = None
        self._user_id = None

        if cc is not None:
            if not isinstance(cc, str):
                raise TypeError(" must be string !!")
            self._cc = cc

        if user_id is not None:
            if not isinstance(user_id, str):
                raise TypeError("must be string !!")
            self._userId = user_id


if __name__ == "__main__":
    s = StringObject("deb", "1122")
    print(s)
