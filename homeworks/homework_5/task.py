import uvicorn
import logging
from enum import Enum
from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# определенные значения из предопределенного набора
class StatusEnum(str, Enum):
    done = "выполнена"
    not_done = "не выполнена"


class Task(BaseModel):
    id: int
    title: str
    description: str
    status: StatusEnum


tasks = [
    Task(
        id=1,
        title="Learn Fastapi",
        description="try to learn Fastapi",
        status=StatusEnum.not_done,
    ),
    Task(
        id=2,
        title="Homework 5",
        description="send to GB",
        status=StatusEnum.done,
    ),
]


# Получение списка всех задач если ID не передан. Получение информации о задаче по её ID.
@app.get("/")
@app.get("/tasks/", response_model=list[Task])
@app.get("/tasks/{task_id}", response_model=list[Task])
async def get_tasks(task_id: int = None):
    if task_id:
        return [task for task in tasks if task.id == task_id]
    return tasks


# Создание новой задачи
@app.post("/tasks/", response_model=Task)
async def create_task(task: Task):
    if [t for t in tasks if t.id == task.id]:
        raise HTTPException(status_code=403, detail="This id is already in use")
    tasks.append(task)
    logger.info(f"Task id={task.id} {task.title} - успешно добавлен")
    return task


# Обновление информации о задаче по её ID.
@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: Task):
    for i, t in enumerate(tasks):
        if t.id == task_id:
            tasks[i] = task
            logger.info(f"Task id={task.id} - успешно изменен")
            return tasks[i]
    raise HTTPException(status_code=404, detail="Task not found")


# Удаление задачи по её ID
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[i]
            logger.info(f"Task id={task.id} {task.title} - успешно удален")
            return {"message": f"Task id={task_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")


# Получение списка задач по статутсу
@app.get("/status/")
async def get_items(status: StatusEnum = Query(None)):
    return [task for task in tasks if task.status == status]


if __name__ == "__main__":
    uvicorn.run("hw4:app", host="localhost", port=8000, reload=True)