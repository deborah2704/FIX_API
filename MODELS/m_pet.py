from MODELS.m_basic import BasicObj
from MODELS.m_category import Category
from MODELS.m_tag import Tags


class Pet(BasicObj):

    def __init__(self, name: str, id: int, category=None, image=None, tags=None, status=None):
        super().__init__()
        self._name = None
        self._id = None
        self._category = None
        self._imageUrl = None
        self._tags = None
        self._status = None
        
        if not isinstance(name, str):
            raise TypeError("must to be string !!!")
        self._name = name
        if not str(id).isdigit():
            raise TypeError("must to be integer !!!")
        self._id = id
        if category is not None:
            if not isinstance(category, Category) and not isinstance(category, dict):
                raise TypeError("must to be instance of Category !!!")
            if isinstance(category, dict):
                category = Category(**category)
            self._category = category
        if image is not None:
            if not isinstance(image, list):
                raise TypeError("must to be a strings!!! ")
            for image_url in image:
                if not isinstance(image_url, str):
                    raise TypeError("error !!!  is not a string!")
            self._imageUrl = image
        if tags is not None:
            if not isinstance(tags, list):
                raise TypeError("the tag must to be a list of Tags!")
            for tag in tags:
                if not isinstance(tag, Tags) and not isinstance(tag, dict):
                    raise TypeError("error !!!")
                if isinstance(tag, dict):
                    tags = Tags(**tag)
            self._tags = tags
        if status is not None:
            if not isinstance(status, str):
                raise TypeError("must to be a string !!!")
            if not status == "avail" and not status == "pending" and not status == "sold":
                raise ValueError("must be one of: available/sold/pending")
            self._status = status

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("must to be a string !!!")
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, Id):
        if not str(Id).isdigit():
            raise TypeError("must to be a integer !!!")
        self._Id = Id


    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if not isinstance(category, Category):
            raise TypeError("must to be instance of Category !!!")
        self._category = category

    @property
    def image_url(self):
        return self._imageUrl

    @image_url.setter
    def photoUrls(self, imageurl):
        if not isinstance(imageurl, list):
            raise TypeError("must to be a strings!!! ")
        for imageurl in imageurl:
            if not isinstance(imageurl, str):
                raise TypeError("error !!!  is not a string!")
        self._imageUrl = imageurl

    @property
    def tag(self) -> list:
        return self._tags

    @tag.setter
    def tag(self, tags):
        if not isinstance(tags, list):
            raise TypeError("must to be a list of Tags!!!")
        for tag in tags:
            if not isinstance(tag, Tags):
                raise TypeError("error!!!")
        self._tags = tags

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if not isinstance(status, str):
            raise TypeError("must to be a string!!!")
        if not status == "valid" and not status == "pending" and not status == "sold":
            raise ValueError("status must be one of: valid/sold/pending")
        self._status = status


def main():
    category = Category("daniCat", 111111)
    t = Tags("daniTag", 111111)
    P = Pet("dani", 111111, category, ["daniel_img", "danish", "de el"], [t], "pending")


if __name__ == '__main__':
    main()


