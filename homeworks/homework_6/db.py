import databases
from sqlalchemy import (
    DECIMAL,
    Date,
    ForeignKey,
    Table,
    Column,
    Integer,
    String,
    MetaData,
    create_engine,
)
from settings import settings

# Создаем БД
DATABASE_URL = settings.DATABASE_URL
db = databases.Database(DATABASE_URL)
metadata = MetaData()

# Таблицы в БД
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("surname", String(50)),
    Column("email", String(50)),
    Column("password", String(30)),
)

items = Table(
    "items",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(50)),
    Column("price", DECIMAL),
)

orders = Table(
    "orders",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("item_id", Integer, ForeignKey("items.id")),
    Column("order_date", Date()),
    Column("status", String(30)),
)


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)