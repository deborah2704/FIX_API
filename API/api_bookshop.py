import requests


class AccountApi:
    def __init__(self, url: str = None, token: str = None):
        if url is None:
            self.url = "https://bookstore.toolsqa.com"
        else:
            self.url = url
        self.token = token
        self.headers = {
            'accept': 'application/json',
            'authorization': 'Basic b21lcm1hem9yMTI6T21lcjEyMyE==true',
            'Authorization': f'Bearer {self.token}'
        }

        self.session = requests.session()
        self.session.headers.update(self.headers)

# POST
    def post_authoriz(self, login_view_model):
        login_view_model_data = login_view_model.to_json()
        res = self.session.post(url=f"{self.url}/Account/v1/Authorized", data=login_view_model_data)
        return res

    def post_generate_tok(self, login_view_model):
        login_view_model_data = login_view_model.to_json()
        res = self.session.post(url=f"{self.url}/Account/v1/GenerateToken", data=login_view_model_data)
        return res

    def post_user(self, register_view_model):
        register_view_model_data = register_view_model.to_json()
        res = self.session.post(url=f"{self.url}/Account/v1/User", data=register_view_model_data)
        return res

# DELETE
    def delete_user_by_id(self, user_id: str):
        res = self.session.delete(url=f"{self.url}/Account/v1/User/{user_id}")
        return res

# GET
    def get_user_by_id(self, user_id: str):
        res = self.session.get(url=f"{self.url}/Account/v1/User/{user_id}")
        return res


class BookShopApi:
    def __init__(self, url=None, token: str = None):
        if url is None:
            self.url = "https://bookstore.toolsqa.com"
        else:
            self.url = url
        self.token = token
        self.headrs = {
            'accept': 'application/json',
            'authorization': 'Basic b21lcm1hem9yMTI6T21lcjEyMyE==true',
            'Authorization': f'Bearer {self.token}'
        }
        self.session = requests.session()
        self.session.headers.update(self.headrs)

# GET
    def get_all_store_of_books(self):
        res = self.session.get(url=f"{self.url}/BookStore/v1/Books")
        return res

    def get_by_isbn(self, isbn: str):
        res = self.session.get(url=f"{self.url}/BookStore/v1/Book?ISBN={isbn}")
        return res

# POST
    def post_book(self, list_of_books):
        list_of_books_data = list_of_books.to_json()
        res = self.session.post(url=f"{self.url}/BookStore/v1/Books", data=list_of_books_data)
        return res

# DELETE
    def delete_book_by_user_id(self, user_id: str):
        res = self.session.delete(url=f"{self.url}/BookStore/v1/Books?UserId={user_id}")
        return res

    def delete_book_by_string_obj(self, str_obj):
        string_object_data = str_obj.to_json()
        res = self.session.delete(url=f"{self.url}/BookStore/v1/Book", data=string_object_data)
        return res

# PUT
    def put_is_bn(self, new_isbn: str, replace_is_bn):
        replace_isbn_data = replace_is_bn.to_json()
        res = self.session.put(url=f"{self.url}/BookStore/v1/Books/{new_isbn}", data=replace_isbn_data)
        return res


