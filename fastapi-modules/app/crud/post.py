from typing import List, Optional
from ..schemas.post import Post

my_list = [
    Post(title="title1", content="content",published=True,ratings=4),
    Post(title="title2", content="content",published=True,ratings=2)
]

def get_all_posts() -> List[Post]:
    return my_list

def get_latest_post() -> Optional[Post]:
    post = my_list[-1]
    return post