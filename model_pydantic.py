import datetime
from typing import List, Optional

from pydantic import BaseModel


order_json = {
    "item_id": "123",
    # "created_date": "2002-11-24 12:22",
    "pages_visited": [1, 2, "3"],
    "price": 17.22,
}


class Order(BaseModel):
    item_id: int
    created_date: datetime.datetime
    pages_visited: Optional[List[int]] = []
    price: float


o = Order(**order_json)
print(o)
