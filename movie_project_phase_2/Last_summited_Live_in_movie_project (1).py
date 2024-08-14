import random
import statistics as stat
from fuzzywuzzy import fuzz, process
import matplotlib.pyplot as plt
import colorama
from colorama import Back, Fore, Style


# Function to add a movie to the dictionary
def add_movie(movies, title, rating, genre):
	title_lower = title.lower()
	if title_lower in movies:
		print(f"Movie {title} already exists.")
	else:
		movie = {"title": title, "rating": rating, "genre": genre}
		movies[title_lower] = movie
		print(f"Added {title} to {genre} with a rating of {rating}.")


# Function to list all movies
def read_movie(movies):
	if not movies:
		print("No movies in the list.")
	else:
		for movie in movies.values():
			print(f"{movie['title']} ({movie['genre']}): {movie['rating']} rating")


# Function to update a movie's details
def update_movie(movies, old_movie_title, new_movie_title, new_movie_rating, new_movie_genre):
	old_movie_title_lower = old_movie_title.lower()
	if old_movie_title_lower in movies:
		movies[old_movie_title_lower] = {
			"title": new_movie_title,
			"rating": new_movie_rating,
			"genre": new_movie_genre
		}
		print(
			f"Updated {old_movie_title} to {new_movie_title} with a rating of {new_movie_rating} in {new_movie_genre}.")
	else:
		print(f"{old_movie_title} is not found.")


# Function to delete a movie from the dictionary
def delete_movie(movies, movie_title):
	movie_title_lower = movie_title.lower()
	movie_titles = list(movies.keys())
	best_match, score = process.extractOne(movie_title_lower, movie_titles, scorer=fuzz.partial_ratio)
	if score >= 50:  # Threshold for a good match
		del movies[best_match]
		print(f"Deleted movie: {best_match.title()} (Score: {score})")
	else:
		print(Fore.RED + f"Movie {movie_title} not found.")


# Function to calculate and print movie statistics
def stats_rating(movies):
	if movies:
		ratings = [movie['rating'] for movie in movies.values()]
		average_rating = stat.mean(ratings)
		median_rating = stat.median(ratings)
		best_movie = max(movies.values(), key=lambda x: x['rating'])
		worst_movie = min(movies.values(), key=lambda x: x['rating'])
		print(f"Average rating: {average_rating:.2f}")
		print(f"Median rating: {median_rating:.2f}")
		print(f"Best rating: {best_movie['rating']} ({best_movie['title']})")
		print(f"Worst rating: {worst_movie['rating']} ({worst_movie['title']})")
		
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


# Function to print a random movie
def list_random(movies):
	if movies:
		random_movie = random.choice(list(movies.values()))
		print(f"Random movie: {random_movie['title']} ({random_movie['genre']}): {random_movie['rating']} rating")
	else:
		print("No movies available.")


# Function to sort and print movies by rating
def sorted_by_rate(movies):
	sorted_movies = sorted(movies.values(), key=lambda x: x['rating'])
	for movie in sorted_movies:
		print(f"Sorted movie: {movie['title']} ({movie['genre']}): {movie['rating']} rating")


# Function to search for a movie by title
def search_movie(movies, movie_title):
	movie_titles = list(movies.keys())
	search_movie_lower = movie_title.lower()
	# This partial fuzzy string ration finds some of the strings match and retrive from the database
	best_match, score = process.extractOne(search_movie_lower, movie_titles, scorer=fuzz.partial_ratio)
	
	if score >= 50:  # Threshold for a good match
		movie = movies[best_match]
		print(f"Found {movie['title']} ({movie['genre']}): {movie['rating']} rating (Score: {score})")
	else:
		print(f"Movie {movie_title} not found.")  # If we "shaw" in search , we found "Shawshank Redemption movie"


# Menu function to interact with the movie database
def menu():
	movies = {
		"the shawshank redemption": {"title": "The Shawshank Redemption", "rating": 9.3, "genre": "Drama"},
		"pulp fiction": {"title": "Pulp Fiction", "rating": 8.9, "genre": "Crime"},
		"the godfather": {"title": "The Godfather", "rating": 9.2, "genre": "Crime"},
		"the dark knight": {"title": "The Dark Knight", "rating": 9.0, "genre": "Action"},
		"forrest gump": {"title": "Forrest Gump", "rating": 8.8, "genre": "Drama"},
		"inception": {"title": "Inception", "rating": 8.8, "genre": "Sci-Fi"},
		"fight club": {"title": "Fight Club", "rating": 8.8, "genre": "Drama"},
		"the matrix": {"title": "The Matrix", "rating": 8.7, "genre": "Sci-Fi"},
		"goodfellas": {"title": "Goodfellas", "rating": 8.7, "genre": "Crime"},
		"interstellar": {"title": "Interstellar", "rating": 8.6, "genre": "Sci-Fi"}
	}
	
	while True:
		print(Fore.GREEN + "\nMenu:")
		print(Fore.BLUE + "1. List movies")
		print(Fore.CYAN + "2. Add movie")
		print(Fore.YELLOW + "3. Delete movie")
		print(Fore.MAGENTA + "4. Update movie")
		print(Fore.WHITE + "5. Stats")
		print(Fore.BLACK + "6. Random movie")
		print(Fore.CYAN + "7. Search movie")
		print(Fore.WHITE + "8. Movies sorted by rating")
		print(Fore.GREEN + "9. Exit")
		
		choice = input("\nEnter choice (1-9): ")
		if choice == "1":
			read_movie(movies)
		elif choice == "2":
			title = input("Enter movie title: ")
			rating = float(input("Enter rating: "))
			genre = input("Enter genre: ")
			add_movie(movies, title, rating, genre)
		elif choice == "3":
			movie_title = input("Enter movie title to delete: ")
			delete_movie(movies, movie_title)
		elif choice == "4":
			old_movie_title = input("Enter current movie title: ")
			new_movie_title = input("Enter new movie title: ")
			new_movie_rating = float(input("Enter new rating: "))
			new_movie_genre = input("Enter new genre: ")
			update_movie(movies, old_movie_title, new_movie_title, new_movie_rating, new_movie_genre)
		elif choice == "5":
			stats_rating(movies)
		elif choice == "6":
			list_random(movies)
		elif choice == "7":
			movie_title = input("Enter movie title to search: ")
			search_movie(movies, movie_title)
		elif choice == "8":
			sorted_by_rate(movies)
		elif choice == "9":
			print("Exiting program...")
			break
		else:
			print("Invalid choice. Please enter a number between 1 and 9.")


menu()

