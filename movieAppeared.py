import requests

# Function to retrieve film titles from URLs
def get_film_titles(urls):
    film_titles = []
    for url in urls:
        response = requests.get(url)
        if response.ok:
            film_data = response.json()
            film_titles.append(film_data['title'])
    return film_titles

# Function to get character information from the API
def get_character_info(character_url):
    response = requests.get(character_url)
    if response.ok:
        character_data = response.json()
        name = character_data['name']
        films = get_film_titles(character_data['films'])
        return name, films
    else:
        return None, None

# API endpoint URL
character_url = "https://swapi.dev/api/people/3/"

# Get character information from the API
character_name, character_films = get_character_info(character_url)

# Print the character's information
if character_name and character_films:
    print("Name:", character_name)
    print("Films:")
    for film_title in character_films:
        print(film_title)
else:
    print("Failed to retrieve character information.")
