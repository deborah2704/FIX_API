import pytest
from MODELS.m_book import Book
from MODELS.m_login import Login
from MODELS.m_register import Register
from MODELS.m_collection import Collection
from MODELS.m_add import Add
from MODELS.m_createUser import CreateUser
from MODELS.m_getUser import GetUser
from MODELS.m_replace import Replace
from MODELS.m_srtObj import StringObject
from API.api_account import AccountApi
from API.api_bookshop import BookShopApi
import logging
import datetime

user_id = open("models/id.txt", "r")
tok = open("models/token.txt", "r")
user_id_r = user_id.read()
tok_r = tok.read()
api_acc = AccountApi("https://bookstore.toolsqa.com", )
api_book = BookShopApi("https://bookstore.toolsqa.com")
bookShopApiTok = BookShopApi("https://bookstore.toolsqa.com", tok_r)
api_acc_tok = AccountApi("https://bookstore.toolsqa.com")
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)
log = logging.getLogger()


# REGISTER
@pytest.fixture()
def My_Details() -> Register:
    register = Register("debi", "DSds2001")
    return register


# LOGIN
@pytest.fixture()
def My_User() -> Login:
    login = Login("debi", "DSds2001")
    return login


# LIST
@pytest.fixture()
def List_book() -> Add:
    c = Collection("12345")
    add_to_list = Add(user_id_r, [c])
    return add_to_list


# BOOK
@pytest.fixture()
def Book() -> Book:
    b = Book("12345", "ugly ducky", "my story", "deborah shoushana", datetime.datetime(2020, 20, 2), "raanana", 321, "animal", "https://www.youtube.com/watch?v=TyrmcD8Yml0")
    return b


# OBJECT STRING
@pytest.fixture()
def String_Obj() -> StringObject:
    user_ID = open("models/id.txt", "r")
    string_object = StringObject("1122334455", user_ID.read())
    return string_object


# REPLACE
@pytest.fixture()
def Replace() -> Replace:
    userID = open("models/id.txt", "r")
    replace = Replace(userID.read(), "abcdefg")
    return replace


# POST
def test_post_user(My_Detail, My_User):
    log.info("testing to create new user")
    res_post_user = api_acc.post_user(My_Detail)
    assert res_post_user.status_code == 201
    assert res_post_user.json()["username"] == My_Detail.userName
    user_ID = open("../Book2/models/id.txt", "w")
    t = open("../Book2/models/token.txt", "w")
    user_ID.write(res_post_user.json()["userID"])
    res_post_tok = api_acc.post_generate_token(My_User)
    t.write(res_post_tok.json()["token"])


def test_post_authoriz(My_User):
    log.info("testing user authorization")
    res_post = api_acc_tok.post_authoriz(My_User)
    assert res_post.status_code == 200
    assert res_post.json() is True


def test_post_generate_token(My_User):
    log.info("testing generate new token")
    res_post = api_acc.post_generate_token(My_User)
    assert res_post.status_code == 200
    tok = open("../Book2/models/token.txt", "w")
    tok.seek(0)
    tok.write(res_post.json()["token"])


# GET USER
def test_get_user_by_id():
    log.info("testing of get user by id")
    res_get = api_acc_tok.get_user_by_id(user_id_r)
    assert res_get.status_code == 200
    log.info(res_get.json()['userId'])


# DELETE USER
def test_delete_user_by_id():
    log.info("testing for delete user by id")
    res_delete = api_acc_tok.delete_user_by_id(user_id_r)
    assert res_delete.status_code == 204
    res_get = api_acc_tok.get_user_by_id(user_id_r)
    assert res_get.status_code == 401


# GET ALL BOOK
def test_get_all_store_books():
    log.info("testing to get all books in the store")
    res_get = api_book.get_all_store_of_books()
    assert res_get.status_code == 200
    log.info(res_get.json())


# POST BOOK
def test_post_book(List_Of_Books):
    log.info("testing to create list of books")
    log.error("error 504 !!!")
    res_delete = bookShopApiTok.delete_book_by_user_id(user_id_r)
    assert res_delete.status_code == 204
    res_post = bookShopApiTok.post_book(List_Of_Books[0])
    assert res_post.status_code == 504
    log.error("504 Gateway Time-out")
    assert res_post.status_code == 201
    log.info(f"Success! {res_post.json()}")


# DELETE BOOK
def test_delete_books_by_userid():
    res_delete = bookShopApiTok.delete_book_by_user_id(user_id_r)
    assert res_delete.status_code == 204
    log.info(res_delete.text)


# GET
def test_get_by_cc():
    log.info("testing for get books by isbn")
    res_get = api_book.get_all_store_of_books()
    assert res_get.status_code == 200
    assert res_get.json()["books"][0]["isbn"]
    res_get2 = api_book.get_by_isbn(res_get.json()["books"][0]["isbn"])
    assert res_get2.status_code == 200
    assert res_get2.json()["isbn"] == res_get.json()["books"][0]["isbn"]


# DELETE BOOK
def test_delete_books_by_string_object(My_String_Object):
    log.info("test for delete books with str object (cc, userid)")
    log.error("ERROR !!!")
    res_get = api_acc_tok.get_user_by_id(user_id_r)
    assert res_get.status_code == 200
    res_post = bookShopApiTok.post_book(My_String_Object[0])  # Post Request Don't Work!!!
    assert res_post.status_code == 201  # Post Request Don't Work!!!
    res_delete = bookShopApiTok.delete_book_by_string_obj(My_String_Object[1])
    res_get2 = api_acc_tok.get_user_by_id(user_id_r)
    assert res_delete.status_code == 204
    log.info("deleted of book successfully!")
    b_before = res_get.json()["books"]
    b_after = res_get2.json()["books"]
    assert len(b_after) < len(b_before)


# PUT
def test_put(My_Replace, My_User):
    userID = open("models/id.txt", "r")
    tok = open("models/token.txt", "r")
    accountApiTok = AccountApi("https://bookstore.toolsqa.com")
    res_post = accountApiTok.post_authoriz(My_User)
    res_get = accountApiTok.get_user_by_id(userID.read())
    print(res_get.json())
