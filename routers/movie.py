from fastapi import APIRouter
# Import Libraries 
from fastapi import Path, Query, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from typing import List
from services.movie import MovieService
from schemas.movie import Movie


# Router Variable
movie_router = APIRouter()


# Get Movie
@movie_router.get('/movies', tags=['movies'], response_model= List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code= 200, content=jsonable_encoder(result))

# Movies ID
@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movie(id: int = Path(ge =1, le = 2000)) -> Movie:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Movie Not Found'})
    return JSONResponse(status_code= 200,content= jsonable_encoder(result))

# Movie Category
@movie_router.get('/movies/', tags=['movies'], response_model= List[Movie])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies_by_category(category)
    return JSONResponse(status_code= 200,content= jsonable_encoder(result))

# Post Method - Create
@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    # movies.append(movie.dict())
    return JSONResponse(status_code=201, content={"message":"It has been successfully registered"})

# PUT Method - Update
@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> dict:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Movie Not Found'})
    
    MovieService(db).update_movie(id, movie)
    return JSONResponse(status_code=200, content={"message":"It has been successfully modified"})
        
# DELETE Method    
@movie_router.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code= 200)
def delete_movie(id: int) -> dict:
    db = Session()
    result = MovieModel = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Movie Not Found'})
    MovieService(db).delete_movie(id)
    return JSONResponse(status_code= 200,content={"message":"It has been successfully deleted"})
            

