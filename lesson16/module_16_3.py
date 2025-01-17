from fastapi import FastAPI, Path
from typing import Annotated
from fastapi import HTTPException

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20,
                    description="Enter username", example="UrbanUser")],
                    age: Annotated[int, Path(ge=18, le=120,
                    description="Enter age", example="24")]) -> str:
    user_id = str(max(int(i[0]) for i in users) + 1 if users else 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[str, Path(min_length=1, max_length=4,
                    description="Enter id", example="10")],
                    username: Annotated[str, Path(min_length=5, max_length=20,
                    description="Enter username", example="UrbanUser")],
                    age: Annotated[int, Path(ge=18, le=120,
                    description="Enter age", example="24")]) -> str:
    for key in users:
        if key == user_id:
            users[key] = f'Имя: {username}, возраст: {age}'
            return f'User {key} has been updated'
    raise HTTPException(status_code=404, detail="user_id не найден")

@app.delete("/users/{user_id}")
async def delete_user(user_id: Annotated[str, Path(min_length=1, max_length=4,
                description="Enter user_id", example="10")]) -> str:
    for key in users:
        if key == user_id:
            users.pop(key)
            return f"User {key} has been deleted"
    raise HTTPException(status_code=404, detail="user_id не найден")

#python -m uvicorn module_16_3:app --reload