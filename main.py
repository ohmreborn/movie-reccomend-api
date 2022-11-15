#  uvicorn main:app --host 0.0.0.0 --port 8000 --reload
# uvicorn main:app --host 165.22.3.172 --port 8000 --reload
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rec import reccomend,get_title,get_genres,multi_reccommend,get_by_id
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def send_message():
    return {"message": "Hello Duke"}
    
@app.get('/id')
def cat_mov(m_id:int):
    return {'data':get_by_id(m_id)}

@app.get('/get-reccom-2')
def get_data_2(title:str):
    return {'data':multi_reccommend(title)}

@app.get('/get-form-genres')
def genres(gen:str):
    return {'data':get_genres(gen)}

@app.get('/get-title')
def get_title_only(title:str):
    return {'data':get_title(title)}

@app.get('show-all-genres')
def show_genres():
    return {'data':['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction', 'TV Movie', 'Thriller', 'War', 'Western']}