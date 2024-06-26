from decimal import Decimal
from pydantic import BaseModel, EmailStr, Field
from enum import Enum
from datetime import date


class Status(str, Enum):
    accepted = "accepted"
    gathering = "gathering"
    send = "send"


class UserIn(BaseModel):
    name: str = Field(..., title="Name", min_length=2, max_length=50)
    surname: str = Field(..., title="Surname", min_length=2, max_length=50)
    email: EmailStr = Field(..., title="Email", max_length=50)
    password: str = Field(..., title="Password")


class User(UserIn):
    id: int


class ItemIn(BaseModel):
    title: str = Field(..., title="title", min_length=2, max_length=50)
    description: str = Field(..., title="description", max_length=300)
    price: Decimal = Field(
        ...,
        title="price",
        ge=0,
        description="Price of the item",
        quant_digits=2,
        decimal_places=2,
    )


class Item(ItemIn):
    id: int


class OrderIn(BaseModel):
    user_id: int = Field(..., title="User id")
    item_id: int = Field(..., title="Item id")
    order_date: date = Field(..., title="Day order", description="YYYY-MM-DD")
    status: Status = Field(
        ..., title="Status", description="accepted - gathering - send"
    )


class Order(OrderIn):
    id: int