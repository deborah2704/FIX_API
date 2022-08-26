from MODELS.m_basic import BasicObj


class Tags(BasicObj):

    def __init__(self, id=None, name=None):
        super().__init__()
        if id is not None:
            if not str(id).isdigit():
                raise TypeError("must to be integer !!!")
            self._id = id
        if name is not None:
            if not isinstance(name, str):
                raise TypeError("must to be string !!!")
            self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("must to be string !!!")
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, Id):
        if not str(Id).isdigit():
            raise TypeError("must to be integer !!!")
        self._id = Id

