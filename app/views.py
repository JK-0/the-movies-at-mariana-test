import json
from datetime import datetime
import pytz
from django.shortcuts import render

def movie_details(request):
    # fetching json file from movies folder
    with open('movies/index.json') as file:
        json_data = json.load(file)

    # Flatten the JSON data to a list of movies
    all_movies = []
    all_movies_by_date = json_data

    for d in all_movies_by_date:
        date_object = datetime.strptime(d['date'], "%Y-%m-%dT%H:%M:%S.%fZ")
        date_object = date_object.replace(tzinfo=pytz.UTC)
        print(date_object)
        
        d['date'] = date_object

    for date_data in json_data:

        all_movies.extend(date_data.get('movies', []))

    # Extract all unique genres from movies data
    all_genres = set()
    for movie in all_movies:
        all_genres.update(movie.get('genre', []))

    # Pass this context to our web page template
    context = {
        'movies': all_movies,
        'all_genres': all_genres,
        'json_data': all_movies_by_date,
    }
    # print(context)
    return render(request, 'movie_template.html', context)
