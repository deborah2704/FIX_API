import json


class BasicObj:

    def __init__(self):
        pass

    def to_json(self) -> str:
        # return json.dumps(self.__dict__)
        res = {}
        for key, val in self.__dict__.items():
            if val is not None:
                if key.startswith("_"):
                    res[key[1:]] = val
                else:
                    res[key] = val
        return res

    def __str__(self):
        return json.dumps(self.to_json())