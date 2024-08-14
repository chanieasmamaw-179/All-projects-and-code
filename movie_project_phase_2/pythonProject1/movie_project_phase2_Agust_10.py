import random
import statistics as stat
from fuzzywuzzy import fuzz, process
import matplotlib.pyplot as plt
import colorama
from colorama import Fore, Style
import argparse
import os
import json

"""
The following script allows users to interact with the movie database
directly from the command line:

1. python movie_project_phase2.py list
2. python movie_project_phase2.py add --title "The Matrix Reloaded" --rating 7.2 --genre "Sci-Fi" --year 2003 --properties Director="The Wachowskis" Duration=138
3. python movie_project_phase2.py delete --title "The Matrix Reloaded"
4. python movie_project_phase2.py update --old-title "The Matrix" --title "The Matrix" --rating 9.0 --genre "Sci-Fi" --year 1999 --properties Duration=136
5. python movie_project_phase2.py stats
6. python movie_project_phase2.py random
7. python movie_project_phase2.py search --title "The Matrix"
8. python movie_project_phase2.py sort
"""

# Define the path to the JSON file for persistent storage
DATA_FILE = 'movies.json'


def load_movies():
	"""Load movies from the JSON file."""
	if os.path.exists(DATA_FILE):
		with open(DATA_FILE, 'r') as file:
			return json.load(file)
	return {}


def save_movies(movies):
	"""Save movies to the JSON file."""
	with open(DATA_FILE, 'w') as file:
		json.dump(movies, file, indent=4)


def add_movie(movies, title, rating, genre, year, **kwargs):
	"""Add a movie with additional properties to the dictionary."""
	title_lower = title.lower()
	if title_lower in movies:
		print(f"Movie {title} already exists.")
	else:
		movie = {"title": title, "rating": rating, "genre": genre, "year": year}
		movie.update(kwargs)  # Add additional properties
		movies[title_lower] = movie
		print(f"Added {title} ({year}) to {genre} with a rating of {rating}. Additional properties: {kwargs}")


def read_movie(movies):
	"""List all movies."""
	if not movies:
		print("No movies in the list.")
	else:
		for movie in movies.values():
			properties = ', '.join([f"{key}: {value}" for key, value in movie.items()])
			print(properties)


def update_movie(movies, old_movie_title, new_movie_title, new_movie_rating, new_movie_genre, new_movie_year, **kwargs):
	"""Update a movie's details including additional properties."""
	old_movie_title_lower = old_movie_title.lower()
	if old_movie_title_lower in movies:
		movie = {
			"title": new_movie_title,
			"rating": new_movie_rating,
			"genre": new_movie_genre,
			"year": new_movie_year
		}
		movie.update(kwargs)  # Update with additional properties
		movies[old_movie_title_lower] = movie
		print(
			f"Updated {old_movie_title} to {new_movie_title} ({new_movie_year}) with a rating of {new_movie_rating} in {new_movie_genre}. Additional properties: {kwargs}")
	else:
		print(f"{old_movie_title} is not found.")


def delete_movie(movies, movie_title):
	"""Delete a movie from the dictionary."""
	movie_title_lower = movie_title.lower()
	movie_titles = list(movies.keys())
	best_match, score = process.extractOne(movie_title_lower, movie_titles, scorer=fuzz.partial_ratio)
	if score >= 50:  # Threshold for a good match
		del movies[best_match]
		print(f"Deleted movie: {best_match.title()} (Score: {score})")
	else:
		print(Fore.RED + f"Movie {movie_title} not found." + Style.RESET_ALL)


def stats_rating(movies):
	"""Calculate and print movie statistics."""
	if movies:
		ratings = [movie['rating'] for movie in movies.values()]
		average_rating = stat.mean(ratings)
		median_rating = stat.median(ratings)
		best_movie = max(movies.values(), key=lambda x: x['rating'])
		worst_movie = min(movies.values(), key=lambda x: x['rating'])
		print(f"Average rating: {average_rating:.2f}")
		print(f"Median rating: {median_rating:.2f}")
		print(f"Best rating: {best_movie['rating']} ({best_movie['title']} - {best_movie['year']})")
		print(f"Worst rating: {worst_movie['rating']} ({worst_movie['title']} - {worst_movie['year']})")
		
		# Plotting the ratings of movies
		titles = [movie['title'] for movie in movies.values()]
		plt.figure(figsize=(6, 4))
		plt.bar(titles, ratings, color='black')
		plt.xlabel('Movies')
		plt.ylabel('Ratings')
		plt.title('Ratings of Movies')
		plt.xticks(rotation=90)
		plt.show()
	else:
		print("No statistics to calculate.")


def list_random(movies):
	"""Print a random movie."""
	if movies:
		random_movie = random.choice(list(movies.values()))
		print(
			f"Random movie: {random_movie['title']} ({random_movie['genre']}, {random_movie['year']}): {random_movie['rating']} rating")
	else:
		print("No movies available.")


def sorted_by_rate(movies):
	"""Sort and print movies by rating."""
	sorted_movies = sorted(movies.values(), key=lambda x: x['rating'])
	for movie in sorted_movies:
		print(f"Sorted movie: {movie['title']} ({movie['genre']}, {movie['year']}): {movie['rating']} rating")


def search_movie(movies, movie_title):
	"""Search for a movie by title."""
	movie_titles = list(movies.keys())
	search_movie_lower = movie_title.lower()
	best_match, score = process.extractOne(search_movie_lower, movie_titles, scorer=fuzz.partial_ratio)
	
	if score >= 50:  # Threshold for a good match
		movie = movies[best_match]
		properties = ', '.join([f"{key}: {value}" for key, value in movie.items()])
		print(f"Found {properties} (Score: {score})")
	else:
		print(Fore.RED + f"Movie {movie_title} not found." + Style.RESET_ALL)


def main():
	"""Command-Line Interface (CLI) for movie database."""
	parser = argparse.ArgumentParser(description="Movie Database CLI")
	
	# Define the arguments for the CLI
	parser.add_argument('command', choices=['list', 'add', 'delete', 'update', 'stats', 'random', 'search', 'sort'],
	                    help="Command to execute")
	
	# Arguments for adding or updating a movie
	parser.add_argument('--title', help="Movie title")
	parser.add_argument('--rating', type=float, help="Movie rating")
	parser.add_argument('--genre', help="Movie genre")
	parser.add_argument('--year', type=int, help="Year of release")
	parser.add_argument('--properties', nargs='*', help="Additional properties in key=value format")
	
	# Arguments for searching, updating, or deleting a movie
	parser.add_argument('--old-title', help="Current title of the movie (for updating)")
	
	# Parse the arguments
	args = parser.parse_args()
	
	# Load movie database
	movies = load_movies()
	
	# Execute the command based on the user's input
	if args.command == 'list':
		read_movie(movies)
	
	elif args.command == 'add':
		if args.title and args.rating and args.genre and args.year:
			additional_properties = {}
			if args.properties:
				for prop in args.properties:
					key, value = prop.split('=')
					additional_properties[key.strip()] = value.strip()
			add_movie(movies, args.title, args.rating, args.genre, args.year, **additional_properties)
			save_movies(movies)
		else:
			print(Fore.RED + "Error: Title, rating, genre, and year are required for adding a movie." + Style.RESET_ALL)
	
	elif args.command == 'delete':
		if args.title:
			delete_movie(movies, args.title)
			save_movies(movies)
		else:
			print(Fore.RED + "Error: Title is required for deleting a movie." + Style.RESET_ALL)
	
	elif args.command == 'update':
		if args.old_title and args.title and args.rating and args.genre and args.year:
			additional_properties = {}
			if args.properties:
				for prop in args.properties:
					key, value = prop.split('=')
					additional_properties[key.strip()] = value.strip()
			update_movie(movies, args.old_title, args.title, args.rating, args.genre, args.year,
			             **additional_properties)
			save_movies(movies)
		else:
			print(
				Fore.RED + "Error: Old title, new title, rating, genre, and year are required for updating a movie." + Style.RESET_ALL)
	
	elif args.command == 'stats':
		stats_rating(movies)
	
	elif args.command == 'random':
		list_random(movies)
	
	elif args.command == 'search':
		if args.title:
			search_movie(movies, args.title)
		else:
			print(Fore.RED + "Error: Title is required for searching a movie." + Style.RESET_ALL)
	
	elif args.command == 'sort':
		sorted_by_rate(movies)
	
	else:
		print(Fore.RED + "Unknown command." + Style.RESET_ALL)


# Run the CLI
if __name__ == '__main__':
	main()
