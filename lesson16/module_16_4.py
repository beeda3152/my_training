from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

users = []

class User(BaseModel):
    id: int = None
    username: str = Field(min_length=5, max_length=20)
    age: int = Field(ge=18, le=120)

@app.get("/users")
def get_users() -> List[User]:
    return users

@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int):
    user_id = (max(i.id for i in users) + 1 if users else 1)
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    print(f"created user {user_id} with name: {username}, age: {age}")
    return user

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail=f"id: {user_id} не найден")

@app.delete("/users/{user_id}")
def delete_message(user_id: int) -> str:
    for i, t in enumerate(users):
        if t.id == user_id:
            del users[i]
            return f"User  with id {user_id} was deleted"
    raise HTTPException(status_code=404, detail=f"User was found with id {user_id}")

#python -m uvicorn module_16_4:app --reload