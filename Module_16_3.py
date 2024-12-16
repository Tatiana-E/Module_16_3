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
    new_user_id = str(int(max(users,key=int)) + 1) if users else 1
    users[new_user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_user_id} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, username: str = Path(min_length=5, max_length=30, description="Enter username", examples="Jenny_Smith"),
                      age: int = Path(ge=18, le=120, description="Enter age",examples="27")):
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id):
    if user_id in users:
        users.pop(str(user_id))
        return f"User {user_id} has been deleted"
    else:
        raise HTTPException(status_code=404, detail='Users not found')


