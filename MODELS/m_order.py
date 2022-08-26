from MODELS.m_basic import BasicObj
import datetime


class Order(BasicObj):

    def __init__(self, id: int, pet_id: int, quantity=None, ship_date=None, status=None, complete=None):
        super().__init__()
        self._id = None
        self._petId = None
        self._quantity = None
        self._shipDate = None
        self._status = None
        self._complete = None
        if not str(id).isdigit():
            raise TypeError("num of order  must be a integer!!!")
        self._id = id
        if not str(pet_id).isdigit():
            raise TypeError("order pet id must be a integer!!!")
        self._petId = pet_id
        if quantity is not None:
            if not str(quantity).isdigit():
                raise TypeError("quantity of order must to be a integer!!!")
            self._quantity = quantity
        if ship_date is not None:
            if not isinstance(ship_date, datetime.datetime):
                raise TypeError("order shipDate must be a datetime!!!")
            self._shipDate = ship_date
        if status is not None:
            if not isinstance(status, str):
                raise TypeError("the status must to be a string!")
            if not status == "placed" and not status == "approved" and not status == "delivered":
                raise ValueError("the status must to be one of: placed/approved/delivered")
            self._status = status
        if complete is not None:
            if not isinstance(complete, bool):
                raise TypeError("the order complete must to be a boolean!!!")
            self._complete = complete

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, Id):
        if not str(id).isdigit():
            raise TypeError("the num of order must to be a integer!")
        self._id = Id

    @property
    def pet_id(self):
        return self._petId

    @pet_id.setter
    def pet_id(self, petId):
        if not str(petId).isdigit():
            raise TypeError("order pet id must be a integer!")
        self._petId = petId

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if not str(quantity).isdigit():
            raise TypeError("the quantity of order must to be a integer!")
        self._quantity = quantity

    @property
    def shipDate(self):
        return self._shipDate

    @shipDate.setter
    def shipDate(self, shipDate):
        if shipDate is None:
            raise ValueError("value Invalid")  # noqa: E501
        if not isinstance(shipDate, datetime.datetime):
            raise TypeError("order shipDate must to be a datetime!")
        self._shipDate = shipDate

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if status is None:
            raise ValueError("value Invalid ")
        if not isinstance(status, str):
            raise TypeError("status must to be a string!")
        if not status == "placed" and not status == "approved" and not status == "delivered":
            raise ValueError("the status must be one of: placed/approved/delivered")
        self._status = status

    @property
    def complete(self):
        return self._complete

    @complete.setter
    def complete(self, complete):
        if complete is None:
            raise ValueError("value Invalid ")
        if not isinstance(complete, bool):
            raise TypeError("the order complete must to be a boolean!")
        self._complete = complete


def main():
    o = Order(3242, 23457, 43534, datetime.datetime.now(), "approved", False)
    print(o.to_json())


if __name__ == '__main__':
    main()
