import json
import requests


req = requests.get("https://swapi.dev/api/people/3/")
print(req.status_code)
character = req.json()
character = json.loads(character)
print(character)
# print(f"Here is the new character {character['name']}" )
# print(character['birth_year'])

# print("Movies appeared in: ")

# for movies in character['films']:
#     req = requests.get(movies)
#     movie = req.json()
#     print(movie['title'])


# def get_film_titles(urls):
#     film_titles = []
#     for url in urls:
#         response = requests.get(url)
#         if response.ok:
#             film_data = response.json()
#             film_titles.append(film_data['title'])
#     return film_titles

# # Main function to retrieve character's films
# def get_character_films(json_data):
#     films_urls = json_data['films']
#     film_titles = get_film_titles(films_urls)
#     return film_titles