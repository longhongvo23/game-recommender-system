import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer

# Load data
games = pd.read_csv('data/steam.csv', sep=",", encoding='utf-8', low_memory=False)
games_img = pd.read_csv('data/steam_media_data.csv', sep=",", encoding='utf-8', low_memory=False)
games_des = pd.read_csv('data/steam_description_data.csv', sep=",", encoding='utf-8', low_memory=False)
game_tag = pd.read_csv('data/steamspy_tag_data.csv', sep=",", encoding='utf-8', low_memory=False)

def get_max_tag(df):
    result = []
    for index, row in df.iterrows():
        appid = row['appid']
        tags = row.drop('appid')
        max_tag = tags.idxmax()
        result.append({'appid':appid,'main_tag':max_tag})
    return pd.DataFrame(result)
main_game_tag = get_max_tag(game_tag)

# Merge dataframes
merged_df = pd.merge(games_img, games_des, how='inner', left_on='steam_appid', right_on='steam_appid')
games = pd.merge(games, merged_df, how='inner', left_on='appid', right_on='steam_appid')
games = pd.merge(games, main_game_tag, how='inner', left_on='appid', right_on='appid')

# Drop những cột không cần thiết
games.drop(columns=['english', 'platforms', 'required_age', 'categories', 'genres', 'achievements',
                     'average_playtime', 'median_playtime', 'steam_appid', 'steam_appid', 
                     'background', 'movies', 'detailed_description', 'about_the_game'], inplace=True)

########################################## Thêm các game hiện tại #######################################################################
games.loc[games['name']=='DARK SOULS™ II','main_tag']= 'dark_fantasy'
games.loc[games['name']=='Sekiro™: Shadows Die Twice','main_tag']= 'dark_fantasy'
games.loc[games['name']=='Sekiro™: Shadows Die Twice','steamspy_tags']= 'Action;Souls-like;Difficult;Dark Fantasy'

new_row = {'appid':1245620, 
'name':'ELDEN RING', 
'release_date':'2022-01-25', 
'developer':'FromSoftware', 
'publisher':'Bandai Namco Entertainment',
'steamspy_tags':'Action;RPG;Open World;Dark Fantasy;Adventure', 
'positive_ratings':280000, 
'negative_ratings':25000, 
'owners':10000000, 
'price':59.99, 
'header_image':'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/header_alt_assets_1.jpg?t=1718379607', 
'screenshots':"[{'id': 0, 'path_thumbnail': 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/ss_c97bcad291f4f45d4be4594f34bd78921d961099.600x338.jpg?t=1718379607', 'path_full': 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/ss_c97bcad291f4f45d4be4594f34bd78921d961099.1920x1080.jpg?t=1718379607'}, {'id': 1, 'path_thumbnail': 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/ss_7bef8e5fb78ee8bd396c5ff17af10731edf52c5f.600x338.jpg?t=1718379607', 'path_full': 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/ss_7bef8e5fb78ee8bd396c5ff17af10731edf52c5f.1920x1080.jpg?t=1718379607'}, {'id': 2, 'path_thumbnail': 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/ss_8234a34c918d101fa0b15f73ca2aed5ac7232dbb.600x338.jpg?t=1718379607', 'path_full': 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/ss_8234a34c918d101fa0b15f73ca2aed5ac7232dbb.1920x1080.jpg?t=1718379607'}, {'id': 3, 'path_thumbnail': 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/ss_b6c4cdb36cebdbd52b97ab6e0851b7d3e41f03b3.600x338.jpg?t=1718379607', 'path_full': 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/ss_b6c4cdb36cebdbd52b97ab6e0851b7d3e41f03b3.1920x1080.jpg?t=1718379607'}, {'id': 4, 'path_thumbnail': 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/ss_b70e156adf9e40aed24c10fb352b7813586e7290.600x338.jpg?t=1718379607', 'path_full': 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/ss_b70e156adf9e40aed24c10fb352b7813586e7290.1920x1080.jpg?t=1718379607'}, {'id': 5, 'path_thumbnail': 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/ss_1e3dfe515c04f4071207f01d62b85a1d6b560ced.600x338.jpg?t=1718379607', 'path_full': 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/ss_1e3dfe515c04f4071207f01d62b85a1d6b560ced.1920x1080.jpg?t=1718379607'}, {'id': 6, 'path_thumbnail': 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/ss_cb9445da232527daf9b7d1d2fcc60fe213f0d7ba.600x338.jpg?t=1718379607', 'path_full': 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/ss_cb9445da232527daf9b7d1d2fcc60fe213f0d7ba.1920x1080.jpg?t=1718379607'}, {'id': 7, 'path_thumbnail': 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/ss_828169fcebebe98bee822bd88ae81b410068a2ba.600x338.jpg?t=1718379607', 'path_full': 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/ss_828169fcebebe98bee822bd88ae81b410068a2ba.1920x1080.jpg?t=1718379607'}, {'id': 8, 'path_thumbnail': 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/ss_1bcbf1da1ddefb169cc69292f043a3573b3390ec.600x338.jpg?t=1718379607', 'path_full': 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/ss_1bcbf1da1ddefb169cc69292f043a3573b3390ec.1920x1080.jpg?t=1718379607'}, {'id': 9, 'path_thumbnail': 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/ss_4eac12f0ba713acbe1afcd19ba29f4cf90324ea1.600x338.jpg?t=1718379607', 'path_full': 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/ss_4eac12f0ba713acbe1afcd19ba29f4cf90324ea1.1920x1080.jpg?t=1718379607'}]", 
'short_description':'THE NEW FANTASY ACTION RPG. Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between.', 
'main_tag':'dark_fantasy'}

games.loc[len(games)] = new_row
########################################## RECOMMENDER ##################################################################################
# Preprocess data for TF-IDF and cosine similarity
def tfidf_matrix(games):
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 1), min_df=1)
    new_tfidf_matrix = tf.fit_transform(games['steamspy_tags'])
    return new_tfidf_matrix

def cosine_sim(matrix):
    new_cosine_sim = linear_kernel(matrix, matrix)
    return new_cosine_sim

import json
def get_path_thumbnails(data):
    path_thumbnails = []
    data_list = json.loads(data.replace("'", "\""))
    path_thumbnails = [item['path_thumbnail'] for item in data_list]
    return path_thumbnails

games['developer'] = games['developer'].str.split(';')
games['publisher'] = games['publisher'].str.split(';')

games['steamspy_tags'] = games['steamspy_tags'].str.split(';')
games['steamspy_tags'] = games['steamspy_tags'].fillna("").astype('str')
tfidf_matrix = tfidf_matrix(games)
cosine_sim = cosine_sim(tfidf_matrix)

indices = pd.Series(games.index, index=games['name']).drop_duplicates()

def get_recommendations(name, cosine_sim=cosine_sim):
    idx = indices[name]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    game_indices = [i[0] for i in sim_scores]
    return games.iloc[game_indices][['appid', 'name', 'short_description', 'developer', 'publisher', 'price', 'steamspy_tags', 'release_date', 'header_image','screenshots']]


################################################ TOP 20 #################################################################################

top20 = games

def calculate_average(owners_range):
    if isinstance(owners_range, str) and '-' in owners_range:
        min_owner, max_owner = map(int, owners_range.split('-'))
        return (min_owner + max_owner) / 2
    else:
        try:
            return float(owners_range)
        except ValueError:
            return None

top20['owners'] = top20['owners'].apply(calculate_average)

top20 = top20.sort_values(by='owners',ascending=False)

top20 = top20.head(20)

############################################### TOP DARK FANTASY #########################################################################
top_dark_fantasy = games
top_dark_fantasy['owners'] = top_dark_fantasy['owners'].apply(calculate_average)
top_dark_fantasy = top_dark_fantasy[top_dark_fantasy['main_tag'] == 'dark_fantasy']

top_dark_fantasy = top_dark_fantasy.sort_values(by='owners',ascending=False)

################################################ TOP FPS #################################################################################

top_fps = games
top_fps['owners'] = top_fps['owners'].apply(calculate_average)
top_fps = top_fps[top_fps['main_tag'] == 'fps']

top_fps = top_fps.sort_values(by='owners',ascending=False)

############################################## TOP ACTION ###############################################################################
top_action = games
top_action['owners'] = top_action['owners'].apply(calculate_average)
top_action = top_action[top_action['main_tag'] == 'action']

top_action = top_action.sort_values(by='owners',ascending=False)

########################################### TOP F2P ################################################################################
top_f2p = games
top_f2p['owners'] = top_f2p['owners'].apply(calculate_average)
top_f2p = top_f2p[top_f2p['main_tag'] == 'free_to_play']

top_f2p = top_f2p.sort_values(by='owners',ascending=False)

########################################### TOP RACING #######################################################################
top_racing = games
top_racing['owners'] = top_racing['owners'].apply(calculate_average)
top_racing = top_racing[top_racing['main_tag'] == 'racing']

top_racing = top_racing.sort_values(by='owners',ascending=False)