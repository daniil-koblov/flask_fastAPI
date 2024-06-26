import logging
from fastapi import APIRouter, HTTPException
from models import Order, OrderIn
from db import db, orders
from typing import List


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


order_router = APIRouter()


@order_router.get("/orders/", response_model=List[Order])
async def get_orders():
    query = orders.select()
    return await db.fetch_all(query)


@order_router.get("/orders/{order_id}", response_model=Order)
async def get_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    existing_order = await db.fetch_one(query)
    if existing_order:
        return await db.fetch_one(query)
    raise HTTPException(status_code=404, detail="order not found")


@order_router.post("/orders/", response_model=Order)
async def create_order(order: OrderIn):
    query = orders.insert().values(**order.model_dump())
    last_id = await db.execute(query)
    logger.info(f"order = {order} added")
    return {"id": last_id, **order.model_dump()}


@order_router.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, new_order: OrderIn):
    query = orders.select().where(orders.c.id == order_id)
    existing_order = await db.fetch_one(query)
    if existing_order:
        query = (
            orders.update()
            .where(orders.c.id == order_id)
            .values(**new_order.model_dump())
        )
        await db.execute(query)
        logger.info(f"order id={order_id} changed")
        return {**new_order.model_dump(), "id": order_id}
    raise HTTPException(status_code=404, detail="order not found")


@order_router.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    existing_order = await db.fetch_one(query)
    if existing_order:
        query = orders.delete().where(orders.c.id == order_id)
        await db.execute(query)
        logger.info(f"order id={order_id} deleted")
        return {"message": f"order id={order_id} deleted"}
    raise HTTPException(status_code=404, detail="order not found")