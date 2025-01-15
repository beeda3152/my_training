from fastapi import FastAPI

# инициализация приложения
app = FastAPI()
#python -m uvicorn module_16_1:app

# маршрут к главной странице
@app.get("/")
async def main() -> dict:
    return {"message": "Главная страница"}


# маршрут к странице администратора
@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}


# маршрут к страницам пользователей
@app.get("/user/{user_id}")
async def user(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


# маршрут к страницам пользователей
@app.get("/user/")
async def some_user(username: str, age: int) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

#user?username='Liliy'&age=123