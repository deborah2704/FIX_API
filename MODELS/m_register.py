from MODELS.m_basicObj import BasicObj
import re


class Register(BasicObj):
    def __init__(self, user: str, passwd: str):
        S_Char = ['$', '#', '@', '!', '*']
        if not isinstance(user, str):
            raise TypeError("user must be string")
        self._userName = user
        if not isinstance(passwd, str):
            raise TypeError("password must be string")
        if len(passwd) < 8:
            raise ValueError("your password must be 8 letters!!!")
        elif re.search('[A-Z]', passwd) is None:
            raise ValueError("your password must have capital letter!!!")
        elif re.search('[a-z]', passwd) is None:
            raise ValueError("your password must have lowercase letter!!!")
        elif re.search('[0-9]', passwd) is None:
            raise ValueError("your password must have a number!!!")
        elif not any(char in S_Char for char in passwd):
            raise ValueError("Your password must have at 1 special character ($, #, @, !, *)")
        self._password = passwd

    @property
    def userName(self):
        return self._userName

    @userName.setter
    def user_name(self, user):

        if user is None:
            raise ValueError("Invalid `userName`, not be `None!!!`")
        if not isinstance(user, str):
            raise TypeError("user must to be string!")
        self._userName = user

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, passwd):
        if passwd is None:
            raise ValueError("Invalid `password`, not be `None!!!`")
        if not isinstance(passwd, str):
            raise TypeError("password must to be string")
        self._password = passwd