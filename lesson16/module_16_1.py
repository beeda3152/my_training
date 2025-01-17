from fastapi import FastAPI

# инициализация приложения
app = FastAPI()
#python -m uvicorn module_16_1:app

# маршрут к главной странице
@app.get("/")
async def main() -> str:
    return ("Главная страница")


# маршрут к странице администратора
@app.get("/user/admin")
async def admin() -> str:
    return ("Вы вошли как администратор")


# маршрут к страницам пользователей
@app.get("/user/{user_id}")
async def user(user_id: int) -> str:
    return f"Вы вошли как пользователь № {user_id}"


# маршрут к страницам пользователей
@app.get("/user/")
async def some_user(username: str, age: int) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

#user?username='Liliy'&age=123