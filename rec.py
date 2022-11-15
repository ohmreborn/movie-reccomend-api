import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
class reccomend():
    def __init__(self):
        self.df = pd.read_csv('movies.csv')
        vec = CountVectorizer()
        self.x = vec.fit(self.df['genre_ids'])
        self.y = self.x.transform(self.df['genre_ids'])

    def rank(self,score,m_id=None):
        self.df['score'] = score

        if m_id is not  None:
            self.df.drop(m_id,axis=0,inplace=True)

        self.df.sort_values(by='score',inplace=True,ascending=False)
        self.df = self.df.head(10)
        self.df = self.df.reset_index(drop=False)
        data = []
        for i in range(10):
            
            data.append(self.df.loc[i].to_dict())
        return data

def get_by_id(mov_id,init=reccomend()):
    df = init.df
    movie = df[df['id'] == int(mov_id)].index.item()
    score = cosine_similarity(init.y,init.y[movie])

    return init.rank(score,[movie])


def multi_reccommend(m_id,init=reccomend()):
    df = init.df
    movie = []
    for m in m_id.split(','):
        i = df[df['id'] == int(m)].index.item()
        movie.append(i)
    u_mov = init.y[movie].sum(axis=0).T
    score = init.y @ u_mov
    return init.rank(score,movie)

def get_title(title,init=reccomend()):
    url = f"https://api.themoviedb.org/3/search/movie?api_key=0b4a78f3f6df40ca3779248e701f90e5&language=en-US&query={title}&page=1&include_adult=false"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    results = response.json()
    if results['total_results'] == 0 :
        return 'there are no movie in this api'
    results = results['results'][0]['id']
    
    score = cosine_similarity(init.y,init.y[results])
    return pd.DataFrame(init.rank(score))['original_title'].tolist()

def get_genres(genres:str,init=reccomend()):
    gen = {'Action': '28', 'Adventure': '12', 'Animation': '16', 'Comedy': '35', 'Crime': '80', 'Documentary': '99', 'Drama': '18', 'Family': '10751', 'Fantasy': '14', 'History': '36', 'Horror': '27', 'Music': '10402', 'Mystery': '9648', 'Romance': '10749', 'Science Fiction': '878', 'TV Movie': '10770', 'Thriller': '53', 'War': '10752', 'Western': '37'}
    genres = genres.split(',')
    inp_gen = []
    for i in genres:
        inp_gen.append(gen[i])
    inp_gen = [",".join(inp_gen)]
    data = init.x.transform(inp_gen)
    score = cosine_similarity(init.y,data)

    return init.rank(score)


if __name__ == "__main__":
    # print(multi_reccommend('167032,16871',reccomend()))
    print(get_title('the avenger',reccomend()))
    # print(get_genres('Action,Adventure',reccomend()))
    
