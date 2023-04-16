from pydantic import BaseModel, Field
from typing import Optional


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=50)
    overview: str = Field(min_length=15, max_length=150)
    year: int = Field(ge=1900, le=2023)
    rating: float = Field(ge=0, le=10)
    category: str
    
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "My Movie",
                "overview": "Movie Description",
                "year": 2023,
                "rating": 9.8,
                "category": "Sci-fi"
            }
        }

