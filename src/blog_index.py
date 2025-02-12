# Sample blog post data
from pydantic import BaseModel
from datetime import datetime
from fasthtml.common import *
from monsterui.all import *

class BlogPost(BaseModel):
    title: str
    date: datetime
    author: str
    content_path: str

def BlogPostItem(post):
    return Div(
        H4(post.title),
        DivFullySpaced(
            P(post.author, cls=TextPresets.muted_sm),
            Time(post.date, cls='text-xs')
        ),
        cls='p-4 border rounded hover:bg-secondary'
    )

blog_posts = [
   BlogPost(title="Awakening", 
            date=datetime(year=2025, month=2, day=11), 
            author="Ken Lee",
            content_path="markdown/awakening.md")
]