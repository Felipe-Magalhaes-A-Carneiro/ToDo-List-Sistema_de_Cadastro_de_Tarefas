from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# coxection with frontend
app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_methods=["*"],
        allow_headers=["*"],
)

# data model base
class Task(BaseModel):
        id: int
        title: str
        description: str
        completed: bool = False

# data base - simple
tasks: List[Task] = []


# roots
@app.get("/")
async def root():
        return{"message": "API FastAPI funcionando com React!"}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
       tasks.append(task)
       return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, update_task: Task):
       for i, t in enumerate(tasks):
              if t.id == task_id:
                     task_id[i] = update_task
                     return update_task
              raise HTMLException(status_code=404, detail='Tarefa não encontrada.')
       
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
       for i, t in enumerate(tasks):
              if t.id == task_id:
                     del task[i]
                     return {"message":"Tarefa deletada com sucesso."}