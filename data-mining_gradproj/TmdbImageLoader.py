import requests
import json

'''
Author: Praveen
Reusable Module: Generated Image URL for the given TMDBID
Usage: Optional as URLs are being added to the database
Note: Very costly Operation as n number of requests will be generated while requesting image
URLs
'''
TMDB_API_KEY='17f591005a4b1416ea2d5b150256b520'
#Get Configuration
config_url= 'http://api.themoviedb.org/3/configuration?api_key={API_KEY}'
movies_url='http://api.themoviedb.org/3/movie/{tmdbid}/images?api_key={API_KEY}'
response=requests.get(config_url.format(API_KEY=TMDB_API_KEY))
config_response=response.json()
base_url=config_response['images']['base_url']
default_postersize=config_response['images']['poster_sizes'][2]
def getImageUrl(movieID):
    try:
        response = requests.get(movies_url.format(tmdbid=movieID,API_KEY=TMDB_API_KEY))
        json_response = response.json()
        file_path=json_response['posters'][0]['file_path']
        image_url='{}{}{}'.format(str(base_url),str(default_postersize),str(file_path))
    except Exception:
        msg=Exception
        print(msg)
    return image_url
# print(getImageUrl(8844))