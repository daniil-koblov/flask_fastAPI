import logging
from fastapi import APIRouter, HTTPException
from models import User, UserIn
from db import db, users
from typing import List
from werkzeug.security import generate_password_hash


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


user_router = APIRouter()


@user_router.get("/users/", response_model=List[User])
async def get_users():
    query = users.select()
    return await db.fetch_all(query)


@user_router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    existing_user = await db.fetch_one(query)
    if existing_user:
        return await db.fetch_one(query)
    raise HTTPException(status_code=404, detail="User not found")


@user_router.post("/users/", response_model=User)
async def create_user(user: UserIn):
    password = generate_password_hash(user.password)
    query = users.insert().values(
        name=user.name, surname=user.surname, email=user.email, password=password
    )
    last_id = await db.execute(query)
    logger.info(f"User = {user} added")
    return {"id": last_id, **user.model_dump()}


@user_router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.select().where(users.c.id == user_id)
    existing_user = await db.fetch_one(query)
    if existing_user:
        password = generate_password_hash(new_user.password)
        query = (
            users.update()
            .where(users.c.id == user_id)
            .values(
                name=new_user.name,
                surname=new_user.surname,
                email=new_user.email,
                password=password,
            )
        )
        await db.execute(query)
        logger.info(f"user id={user_id} changed")
        return {**new_user.model_dump(), "id": user_id}
    raise HTTPException(status_code=404, detail="User not found")


@user_router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    existing_user = await db.fetch_one(query)
    if existing_user:
        query = users.delete().where(users.c.id == user_id)
        await db.execute(query)
        logger.info(f"user id={user_id} deleted")
        return {"message": f"user id={user_id} deleted"}
    raise HTTPException(status_code=404, detail="User not found")