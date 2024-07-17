from random import randrange
from typing import List
from fastapi import APIRouter, HTTPException, status

from ..schemas.post import Post
from ..crud.post import get_all_posts, get_latest_post

router = APIRouter()

my_list = [
    Post(title="title1", content="content",published=True,ratings=4),
    Post(title="title2", content="content",published=True,ratings=2)
]
# Read
@router.get("/posts", response_model=List[Post])
def read_all_users():
    return get_all_posts()

@router.get("/posts/latest")
def read_latest_post():
    return get_latest_post()

@router.get("/posts/{id}")
def read_post_by_id(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with ID {id} not found")
    return {"post_detail": post}

# Create
@router.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    my_list.append(post_dict)
    return {"data": post_dict}

# Update
@router.put("/posts/{id}")
def update_post(id: int, post: Post):
    indx = find_index_post(id)
    if indx is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with ID {id} does not exist")
    post_dict = post.dict()
    post_dict['id'] = id
    my_list[indx] = post_dict
    return {"message": f"Post with ID {id} successfully updated"}

@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    indx = find_index_post(id)
    if indx is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with ID {id} does not exist")
    my_list.pop(indx)
    return {"message": f"Post with ID {id} successfully deleted"}

def find_post(id):
    for p in my_list:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_list):
        if p['id'] == id:
            return i