from fastapi import FastAPI, HTTPException, Request, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import List, Annotated
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Настраиваем Jinja2 для загрузки шаблонов из папки templates
templates = Jinja2Templates(directory="templates")

users: List['User'] = []

class User(BaseModel):
    id: int = 0
    username: str
    age: int

@app.get("/", response_class=HTMLResponse)
def get_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}", response_class=HTMLResponse)
def get_user(request: Request, user_id: Annotated[int, Path(ge=1)] ):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request":request, "user": user})
    raise HTTPException(status_code=404, detail="User not found")


@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20,
                    description="Enter username", example="UrbanUser")],
                      age: Annotated[int, Path(ge=18, le=120,
                    description="Enter age", example="24")]):
    user_id = (max(i.id for i in users) + 1 if users else 1)
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    print(f"created user {user_id} with name: {username}, age: {age}")
    return user

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=1)],
                      username: Annotated[str, Path(min_length=5, max_length=20,
                        description="Enter username", example="UrbanUser")],
                      age: Annotated[int, Path(ge=18, le=120,
                         description="Enter age", example="24")]):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail=f"id: {user_id} не найден")

@app.delete("/users/{user_id}")
def delete_message(user_id: Annotated[int, Path(ge=1)]) -> str:
    for i, t in enumerate(users):
        if t.id == user_id:
            del users[i]
            return f"User  with id {user_id} was deleted"
    raise HTTPException(status_code=404, detail=f"User was found with id {user_id}")

#python -m uvicorn module_16_5:app --reload