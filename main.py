# Import Libraries 
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from utils.jwt_manager import create_token
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router


# from fastapi import FastAPI, HTTPException
app = FastAPI()
# To change App's Name
app.title = "Movies FastAPI's App"
# To change App's Version
app.version = "0.0.1"

# Setting MiddleWare Up
app.add_middleware(ErrorHandler)
# Movie APIRouter Call-Up
app.include_router(movie_router)
# User APIRouter Call-Up
app.include_router(user_router)

Base.metadata.create_all(bind=engine)


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
        'title': 'Contact',
        'overview': "Dr. Ellie Arroway races to interpret a possible message originating from the Vega star system. Once first contact with an extraterrestrial intelligence is",
        'year': '1997',
        'rating': 7.5,
        'category': 'Sci-fi'    
    } 
]

# set the action to an endpoint Tags allows to group the app routes
@app.get('/', tags =['Home'])
def message():
    return HTMLResponse('<h1>Welcome to The Movie App!</h1>')

