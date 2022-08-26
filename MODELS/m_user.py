from MODELS.m_basic import BasicObj


class User(BasicObj):

    def __init__(self, id: int, user_name: str, passwd: str, first_name=None, last_name=None, mail=None, tel=None, statos_user=None):
        super().__init__()
        self._id = None
        self._username = None
        self._password = None
        self._firstName = None
        self._lastName = None
        self._gmail = None
        self._telephon = None
        self._statususer = None
        if not str(id).isdigit():
            raise TypeError("must be a integer!!!")
        self._id = id

        if not isinstance(user_name, str):
            raise TypeError("must be a string!!!")
        self._username = user_name

        if not isinstance(passwd, str):
            raise TypeError("must be a string!!!")
        self._password = passwd
        if first_name is not None:
            if not isinstance(first_name, str):
                raise TypeError("must be a string!!!")
            self._firstName = first_name

        if last_name is not None:
            if not isinstance(last_name, str):
                raise TypeError("must be a string!!!!")
            self._lastName = last_name

        if mail is not None:
            if not isinstance(mail, str):
                raise TypeError("must be a string!!!!")
            self._gmail = mail

        if tel is not None:
            if not str(tel).isdigit():
                raise TypeError("must be a integer!!!!")
            self._telephon = tel

        if statos_user is not None:
            if not str(statos_user).isdigit():
                raise TypeError("must be a integer!!!!")
            self._statususer = statos_user

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if username is None:
            raise ValueError("value Invalid")
        if not isinstance(username, str):
            raise TypeError("must be a string!!!!!")
        self._username = username

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, Id):
        if not str(Id).isdigit():
            raise TypeError("must be a integer!!!!")
        self._id = Id

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        if password is None:
            raise ValueError("value Invalid")
        if not isinstance(password, str):
            raise TypeError("must be a string!!!!")
        self._password = password

    @property
    def firstName(self):
        return self._firstName

    @firstName.setter
    def firstName(self, firstName):
        if firstName is None:
            raise ValueError("value Invalid")
        if not isinstance(firstName, str):
            raise TypeError("must be a string!!!!")
        self._firstName = firstName

    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self, lastName):
        if lastName is None:
            raise ValueError("value Invalid")
        if not isinstance(lastName, str):
            raise TypeError("must be a string!!!!")
        self._lastName = lastName

    @property
    def email(self):
        return self._gmail

    @email.setter
    def email(self, email):
        if email is None:
            raise ValueError("value Invalid")
        if not isinstance(email, str):
            raise TypeError("must be a string!!!!")
        self._gmail = email

    @property
    def numberTel(self):
        return self._telephon

    @numberTel.setter
    def numberTel(self, tel):
        if tel is None:
            raise ValueError("value Invalid")
        if not str(tel).isdigit():
            raise TypeError("must be a integer !!!")
        self._telephon = tel

    @property
    def userStatus(self):
        return self._statususer

    @userStatus.setter
    def userStatus(self, userStatus):
        if userStatus is None:
            raise ValueError("value Invalid")
        if not str(userStatus).isdigit():
            raise TypeError("must be a integer !!!")
        self._statususer = userStatus


def main():
    us = User("330163249", "deborah2001", "ds2001", "shoushana", "deborah", "deborah270401@gmail.com", 0, 10)
    print(us)


if __name__ == '__main__':
    main()




