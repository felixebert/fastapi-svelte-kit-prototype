# in memory store of fixed datasets
from typing import Optional, List
from .schemas import User, Product
from os.path import dirname, abspath, join
import json


def load_datasets():
    print("load fixed datasets from database.json")
    with open(join(dirname(abspath(__file__)), "..", "db", "database.json"), "r") as fp:
        return json.load(fp)


class UserInDB(User):
    hashed_password: str


db = load_datasets()


def get_user(username: str) -> Optional[UserInDB]:
    matching_user = list(filter(lambda user: user['username'] == username, db['users']))
    if len(matching_user) == 0:
        return None
    if len(matching_user) > 1:
        raise RuntimeError("multiple matching users")

    return UserInDB(**matching_user[0])


def get_products() -> List[Product]:
    return db['products']
