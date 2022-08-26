from MODELS.m_basicObj import BasicObj
from MODELS.m_collection import Collection


class Add(BasicObj):
    def __init__(self, user_id: str, collection: list):
        self._collection = None
        if user_id is not None:
            if not isinstance(user_id, str):
                raise TypeError("user id must to be string")
            self._userId = user_id

        if collection is not None:
            if not isinstance(collection, list):
                raise TypeError("collection must to be list")
            for cc in collection:
                if not isinstance(cc, collection):
                    raise TypeError("does not exist in the collection!")
            self._collection = collection


if __name__ == "__main__":
    a = Add("ab", ["abc ", "aba"])
    print(a)
