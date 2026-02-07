from pydantic import BaseModel
from datetime import datetime, date
from typing import List
from src.reviews.schema import ReviewModel
from src.tags.schema import TagModel, TagCreateModel
import uuid

class Book(BaseModel):
    uid: uuid.UUID 
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    user_uid: uuid.UUID
    created_at: datetime
    updated_at: datetime

class BookDetailModel(Book):
    reviews: List[ReviewModel]
    tags: List[TagModel]

class BookTagsModel(Book):
    tags: List[TagCreateModel]

class BookCreateModel(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
    
class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str
