from datetime import datetime
from typing import Optional
import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from core.config import settings
from domain.user import User, UserCreate, UserUpdate
from application.services.user_service import UserService
from infraestructura.adapters.memory_user_repository import MemoryUserRepository

app = FastAPI()

posts = []

#post model
class Post(BaseModel):
    id: Optional[str]
    nombre: str
    email: str
    created_at: datetime = datetime.now()

@app.get("/")
def read_root():
    return {"Welcome": "I suffer from depression"}

@app.get("/posts")
def get_posts(): 
    return posts

@app.post("/posts")
def save_post(post: Post):
    post.id = str(uuid.uuid4())
    posts.append(post.dict())
    return posts[-1]

@app.get('/posts/{post_id}')
def get_post(post_id: str):
    for post in posts:
        if post['id'] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")

@app.delete('/posts/{post_id}')
def delete_post(post_id: str):
    for index, post in enumerate(posts):
       if post['id'] == post_id:
           posts.pop(index)
           return {"message": "Post deleted successfully"}
    raise HTTPException(status_code=404, detail="Post not found")

@app.put('/posts/{post_id}')
def update_post(post_id: str, updated_post: Post):
    for index, post in enumerate(posts):
        if post['id'] == post_id:
            posts[index]["nombre"] = updated_post.nombre
            posts[index]["email"] = updated_post.email
            return {"message": "Post updated successfully"}
    raise HTTPException(status_code=404, detail="Post not found")