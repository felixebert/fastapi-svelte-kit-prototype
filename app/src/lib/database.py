# in memory store of fixed datasets
from functools import reduce
from typing import Optional, List
from .schemas import User, Product, Order, OrderRequest, OrderItem, OrderItemRequest
from .config import settings
from .crypt import get_password_hash
from os.path import dirname, abspath, join, exists
from decimal import Decimal, ROUND_HALF_UP
import json

db_file = join(dirname(abspath(__file__)), "..", "db", "database.json")


def load_datasets():
    if settings.DATABASE is not None:
        return json.loads(settings.DATABASE)
    elif exists(db_file):
        print("load fixed datasets from database.json")
        with open(db_file, "r") as fp:
            return json.load(fp)
    else:
        return {
            "users": [],
            "products": []
        }


class UserInDB(User):
    hashed_password: str


db = load_datasets()
db['orders'] = list()
next_order_id = 1


def get_user(username: str) -> Optional[UserInDB]:
    matching_user = list(filter(lambda user: user['username'] == username, db['users']))
    if len(matching_user) == 0:
        return None
    if len(matching_user) > 1:
        raise RuntimeError("multiple matching users")

    user = matching_user[0]
    if 'password' in user:
        return UserInDB(**user, hashed_password=get_password_hash(user['password']))
    else:
        return UserInDB(**user)


def get_products() -> List[Product]:
    return list(map(lambda p: Product(**p), db['products']))


# order request from user only contains product id and quantity per item
# enrich all order items to contain more product details, a total price etc.
def convert_order_items(items: List[OrderItemRequest]) -> List[OrderItem]:
    products = get_products()

    def to_item(item_request: OrderItemRequest) -> OrderItem:
        matching_products = list(filter(lambda p: p.id == item_request.id, products))
        if len(matching_products) <= 0:
            raise ValueError("invalid product")
        product = matching_products[0]
        total = (Decimal(product.price) * Decimal(item_request.quantity)) \
            .quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
        order_item = OrderItem(
            quantity=item_request.quantity,
            total=total,
            **product.dict()
        )
        return order_item

    return list(map(to_item, items))


def add_order(order_request: OrderRequest, user: User) -> Order:
    global next_order_id
    items = convert_order_items(order_request.items)
    order = Order(
        id=next_order_id,
        label="#" + str(next_order_id + 1000),
        user_id=user.id,
        shipping_address=order_request.shipping_address,
        items=items,
        total=reduce(lambda x, y: x + y.total, items, 0)
    )

    db['orders'].append(order)
    next_order_id += 1
    return order
