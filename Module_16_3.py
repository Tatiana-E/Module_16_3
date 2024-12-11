from fastapi import FastAPI, HTTPException, Path
from typing import  Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: str = Path(min_length=5, max_length=30, description="Enter your name", examples="Jenny_Smith")
                         , age: int = Path(ge=18, le=120, description="Enter your age",examples="27")):
    new_user_id = max(user['id'] for user in users) + 1 if users else 1
    users[new_user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_user_id} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id:int, username: str = Path(min_length=5, max_length=30, description="Enter username", examples="Jenny_Smith"),
                      age: int = Path(ge=18, le=120, description="Enter age",examples="27")):
    for user in users:
        if user['id'] in users:
            users[user_id] = f"Имя: {username}, возраст: {age}"
            return f"The user {user_id} is updated"
        raise HTTPException(status_code=404, detail="Пользователь не найден")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    users.pop(str(user_id))
    return f"User {user_id} has been deleted"

