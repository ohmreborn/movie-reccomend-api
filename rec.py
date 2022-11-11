import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
def reccomend(title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key=0b4a78f3f6df40ca3779248e701f90e5&language=en-US&query={title}&page=1&include_adult=false"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    results = response.json()
    if results['total_results'] == 0 :
        return 'there are no movie in this api'
    results = results['results'][0]['original_title']


    
    df = pd.read_csv('movies.csv')
    # df = df[['genre_ids','original_title']]
    movie = df[df['original_title'] == results ]['original_title'].index.item()

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df['genre_ids'])
    score = cosine_similarity(X,X[movie])

    df['score'] = score
    df.drop([movie],axis=0,inplace=True)
    df.sort_values(by='score',inplace=True,ascending=False)
    df = df.head(10)
    df = df.reset_index(drop=False)
    data = []
    for i in range(10):
        
        data.append(df.loc[i].to_dict())
    return data

def multi_reccommend(title):
    total_results = 0
    all_movies = []
    for m in title.split(','):
        url = f"https://api.themoviedb.org/3/search/movie?api_key=0b4a78f3f6df40ca3779248e701f90e5&language=en-US&query={m}&page=1&include_adult=false"

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        results = response.json()
        total_results += int(results['total_results'])
        results = results['results'][0]['original_title']
        all_movies.append(results)

    if total_results == 0 :
            return 'there are no movie in this api'

    df = pd.read_csv('movies.csv')
        
    movies = []
    for i in all_movies:
        movie = df[df['original_title'] == i].index.tolist()[0]
        movies.append(movie)
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df['genre_ids']) 
    genres = X[movies].toarray().sum(axis=0).reshape(-1,1)
    df['score'] = X @ genres
    df.drop(movies,axis=0,inplace=True)
    df.sort_values(by='score',inplace=True,ascending=False)
    df = df.head(10)
    df = df.reset_index(drop=False)
    data = []
    for i in range(10):
        
        data.append(df.loc[i].to_dict())
    return data

def get_title(title):
    data = reccomend(title)
    if data == 'there are no movie in this api':
        return data
    
    movie = []
    for i in data:
        movie.append(i['original_title'])
    return movie

def get_genres(genres:str):
    gen = {'Action': '28', 'Adventure': '12', 'Animation': '16', 'Comedy': '35', 'Crime': '80', 'Documentary': '99', 'Drama': '18', 'Family': '10751', 'Fantasy': '14', 'History': '36', 'Horror': '27', 'Music': '10402', 'Mystery': '9648', 'Romance': '10749', 'Science Fiction': '878', 'TV Movie': '10770', 'Thriller': '53', 'War': '10752', 'Western': '37'}
    genres = genres.split(',')
    inp_gen = []
    for i in genres:
        inp_gen.append(gen[i])
    inp_gen = ",".join(inp_gen)

    df = pd.read_csv('movies.csv')

    vectorizer = CountVectorizer()
    X = vectorizer.fit(df['genre_ids'])
    data = X.transform(df['genre_ids'])
    movie = X.transform([inp_gen])
    score = cosine_similarity(data,movie)

    df['score'] = score
    df.sort_values(by='score',inplace=True,ascending=False)
    df = df.reset_index(drop=True)
    df = df.iloc[:10]
    
    data = []
    for i in range(10):
        
        data.append(df.loc[i].to_dict())

    return data

def show_move():
    df = pd.read_csv('movies.csv').head()
    data = []
    for i in range(5):
        data.append(df.loc[i].to_dict())

    return data
if __name__ == "__main__":
    print(multi_reccommend('thor,the avenger'))
    
