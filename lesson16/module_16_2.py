from fastapi import FastAPI, Path
from typing import Annotated

# инициализация приложения
app = FastAPI()
#python -m uvicorn module_16_2:app --reload

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
async def user(user_id: Annotated[int, Path(ge=1, le=100,
                description="Enter User ID", example="1")]) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


# маршрут к страницам пользователей
@app.get("/user/{username}/{age}")
async def some_user(username: Annotated[str, Path(min_length=5, max_length=20,
                description="Enter username", example="UrbanUser")],
                    age: Annotated[int, Path(ge=18, le=120,
                description="Enter age", example="24")]) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

# username - строка, age - целое число.
# username ограничение по длине: больше или равно 5 и меньше либо равно 20.
# age ограничение по значению: больше или равно 18 и меньше либо равно 120.
# Описания для username и age - 'Enter username' и 'Enter age' соответственно.
# Примеры для username и age - 'UrbanUser' и '24' соответственно. (можете подставить свои примеры не противоречащие валидации).

