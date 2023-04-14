# Import Libraries 
from fastapi import FastAPI, Body, Path, Query, Request,HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer

# from fastapi import FastAPI, HTTPException

app = FastAPI()
# To change App's Name
app.title = "My FastAPI's Application"
# To change App's Version
app.version = "0.0.1"

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Invalid Credentials")

class User(BaseModel):
    email: str
    password: str

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
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

movies = [
    {
        'id': 1,
        'title': 'What Dreams May Come',
        'overview': "After Chris Nielsen dies in a car accident, he is guided through the afterlife by his spirit guide, Albert. His new world is beautiful and can be whatever Chris imagines",
        'year': '1998',
        'rating': 6.9,
        'category': 'Fantasy/Romance'    
    },
    {
        'id': 2,
        'title': 'The Hitchhikers Guide to the Galaxy',
        'overview': "Arthur Dent is trying to prevent his house from being bulldozed when his friend Ford Prefect whisks him into outer space. It turns out Ford is an alien who",
        'year': '2005',
        'rating': 6.8,
        'category': 'Sci-fi'    
    },
   {
        'id': 3,
        'title': 'Contact',
        'overview': "Dr. Ellie Arroway races to interpret a possible message originating from the Vega star system. Once first contact with an extraterrestrial intelligence is",
        'year': '1997',
        'rating': 7.5,
        'category': 'Sci-fi'    
    } 
]


# set the action to an endpoint
# Tags allows to group the app routes
@app.get('/', tags =['Home'])
def message():
    return HTMLResponse('<h1>Hello World!</h1>')

#User Login
@app.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code= 200, content=token)


# Get Movie
@app.get('/movies', tags=['movies'], response_model= List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    return JSONResponse(status_code= 200, content=movies)

@app.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movie(id: int = Path(ge =1, le = 2000)) -> Movie:
    for item in movies:
        if item["id"] == id:
            return JSONResponse(content=item)
        return JSONResponse(status_code= 404,content= [])

@app.get('/movies/', tags=['movies'], response_model= List[Movie])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Movie]:
    data = [item for item in movies if item['category'] == category]
    return JSONResponse(content= data)

# Post Method - Create

@app.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    movies.append(movie.dict())
    return JSONResponse(status_code=201, content={"message":"It has been successfully registered"})

# PUT Method - Update

@app.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> dict:
    for item in movies:
        if['id'] == id:
            item['title'] == movie.title
            item['overview'] == movie.overview
            item['year'] == movie.year
            item['rating'] == movie.rating,
            item['category'] == movie.category
            return JSONResponse(status_code=200, content={"message":"It has been successfully modified"})
        
# DELETE Method
        
@app.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code= 200)
def delete_movie(id: int) -> dict:
    for item in movies:
        if['id'] == id:
            movies.remove(item)
            return JSONResponse(status_code= 200,content={"message":"It has been successfully deleted"})
            

