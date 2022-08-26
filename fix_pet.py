import json
import datetime
import logging
import pytest

import API.api_pet as pet_api
import API.api_order as order_api
import API.api_user as user_api
from MODELS.m_pet import Pet
from MODELS.m_category import Category
from MODELS.m_tag import Tags
from MODELS.m_order import Order
from MODELS.m_user import User

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()

petApi = pet_api.PetApi("https://petstore3.swagger.io/api/v3")
userApi = user_api.UserApi("https://petstore3.swagger.io/api/v3/user")
orderApi = order_api.OrderApi("https://petstore3.swagger.io/api/v3/store")


@pytest.fixture()
def M_Pet() -> Pet:
    category = Category(234, "Cat")
    photoUrls = ["https://en.wikipedia.org/wiki/Cat#/media/File:Cat_poster_1.jpg"]
    tags = [Tags(3453445, "tag1")]
    mitzi = Pet(20, "mitzihahatoul", category, photoUrls, tags, "available")
    return mitzi


@pytest.fixture()
def MOrder() -> Order:
    my_order = Order(1111, 1111, 1, datetime.datetime.now(), "placed", False)
    return my_order


@pytest.fixture()
def MUser() -> User:
    my_user = User(330163429, "deborah2001", "ds270401", "shoushana", "deborah", "deborah270401@gmail.com", +585123646, 10)
    return my_user


@pytest.fixture()
def MUsers() -> [User]:
    user1 = User(222, "danish123", "dash22", "danish", "shoushana", "danish@gmail.com", +585123646, 11)
    user2 = User(32454, "daniel123", "dani21", "daniel", "sadoun", "daniel@gmail.com", +585123646, 12)
    users = [user1, user2]
    return users




# UPLOAD
def test_upload_image_id(MPet):
    log.info("testing upload image by id")
    files = {'upload_file': open('hgfhdh.jpg', 'qq')}
    res_post = petApi.upload_image_by_id(MPet.id, files)
    assert res_post.status_code == 200
    log.info(res_post.json()["message"])
    assert files in petApi.get_pet_by_id(MPet.id)[1].photoUrls


# TEST POST
def test_post_new_pet(MPet):
    log.info("testing post new pet")
    res_post = petApi.post_new_pet(MPet)
    assert res_post.status_code == 200
    res_get = petApi.get_pet_by_id(MPet.id)
    assert res_get.status_code == 200
    assert res_get.json() == res_post.json()


def test_post_pet_id_and_update(MPet):
    log.info("testing post pet by id and update")
    petApi.post_new_pet(MPet)
    pet_before = [MPet.name, MPet.status]
    MPet.name = "danish"
    MPet.status = "sold"
    pet_after = [MPet.name, MPet.status]
    res_post = petApi.post_pet_by_id(MPet.id, MPet.name, MPet.status)
    assert res_post.status_code == 200
    assert res_post.json()["name"] != pet_before[0] and res_post.json()["status"] != pet_before[1]
    assert res_post.json()["name"] == pet_after[0] and res_post.json()["status"] == pet_after[1]


def test_post_order(MOrder):
    log.info("testing post order")
    orderApi.delete_order(MOrder.id)
    res_post = orderApi.post_order(MOrder)
    assert res_post.status_code == 200
    res_get = orderApi.get_order(MOrder.id)
    print(res_get.json())
    assert res_get.status_code == 200
    assert res_get.json() == res_post.json()


def test_post_user(MUser):
    log.info("testing post user")
    userApi.delete_username(MUser.username)
    res_post = userApi.post_user(MUser,)
    assert res_post.status_code == 200
    res_get = userApi.get_username(MUser.username)
    assert res_get.status_code == 200
    assert res_get.json() == res_post.json()


def test_post_users(MUsers):
    log.info("testing create a list of new users")
    users = [user.to_json() for user in MUsers]
    users_json = json.dumps(users)
    res_post = userApi.post_users_list(users_json)
    assert res_post.status_code == 200
    for user_dict in MUsers:
        assert user_dict == userApi.get_username(user_dict['username'])[1].to_json()


# TEST GET
def test_get_pet_byid(MPet):
    log.info("testing get pet by id")
    petApi.post_new_pet(MPet)
    res_get = petApi.get_pet_by_id(MPet.id)
    assert res_get.status_code == 200
    assert res_get.json()["id"] == MPet.id


def test_get_pets_status(MPet):
    log.info("testing get pet by status")
    res_get = petApi.get_pet_by_status(MPet.status)
    assert res_get.status_code == 200
    statusArray = []
    for pet in res_get.json():
        statusArray.append(pet["status"])
    assert MPet.status in statusArray


def test_get_pet_tags(MPet):
    log.info("testing get pet by tags")
    tags = []
    print(MPet.tag[0].name)
    for tag in MPet.tag:
        print(tag.name)
        tags.append(tag.name)
    res_get = petApi.get_pet_by_tags(tags)
    assert res_get.status_code == 200
    tagsNames = []
    for pet in res_get.json():
        for tag in pet["tags"]:
            if isinstance(tag, dict):
                tagsNames.append(tag["name"])
    assert MPet.tag[0].name in tagsNames


def test_get_store_inventory():
    log.info("testing get store inventory")
    res_get = orderApi.get_store_inventory()
    assert res_get.status_code == 200
    assert type(res_get.json()) == dict


def test_get_order(MOrder):
    log.info("testing get order")
    res_get = orderApi.get_order(MOrder.id)
    assert res_get.status_code == 200
    assert res_get.json()["id"] == MOrder.id


def test_get_login(MUser):
    log.info("testing get login")
    print(user_api.UserApi()._url)
    res_get = user_api.UserApi().get_login(MUser.username, MUser.password)
    assert res_get.status_code == 200


def test_get_logout():
    log.info("testing get logout")
    res_get = user_api.UserApi().get_logout()
    assert res_get.status_code == 200


def test_get_username(MUser):
    log.info("testing get username")
    res_post = userApi.post_user(MUser)
    assert res_post.status_code == 200
    res_get = userApi.get_username(MUser.username)
    assert res_get.status_code == 200
    assert res_get.json()["username"] == MUser.username


# TEST PUT
def test_put_pet(MPet):
    log.info("testing put pet")
    re = petApi.post_new_pet(MPet)
    print(re.url)
    MPet.name = "deborah"
    res_put = petApi.put_pet(MPet)
    res_get = petApi.get_pet_by_id(MPet.id)
    assert res_put.status_code == 200
    assert MPet.name == res_get.json()["name"]


def test_put_username(MUser):
    log.info("testing put username")
    res_post = userApi.post_user(MUser)
    assert res_post.status_code == 200
    username = MUser.username
    MUser.username = "Deborah"
    res_put = userApi.put_username(username, MUser)
    assert res_put.status_code == 200
    assert res_put.json()["username"] == MUser.username


# TEST DELETE
def test_delete_pet_id(MPet):
    log.info("testing delete pet by id")
    res_post = petApi.post_new_pet(MPet)
    assert res_post.status_code == 200
    res_delete = petApi.delete_pet(MPet.id)
    assert res_delete.status_code == 200
    res_get = petApi.get_pet_by_id(MPet.id)
    assert res_get.status_code == 404


def test_delete_order(MOrder):
    log.info("testing delete order")
    res_post = orderApi.post_order(MOrder)
    assert res_post.status_code == 200
    res_delete = orderApi.delete_order(MOrder.id)
    assert res_delete.status_code == 200
    res_get = orderApi.get_order(MOrder.id)
    assert res_get.status_code == 404


def test_delete_username(MUser):
    log.info("testing delete username")
    res_post = userApi.post_user(MUser)
    assert res_post.status_code == 200
    res_delete = userApi.delete_username(MUser.username)
    assert res_delete.status_code == 200
    res_get = userApi.get_username(MUser.username)
    assert res_get.status_code == 404

