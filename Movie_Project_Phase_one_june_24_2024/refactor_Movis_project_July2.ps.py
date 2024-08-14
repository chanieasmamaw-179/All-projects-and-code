import random

# It defines a function named create that takes three parameters: movies, genre, and movie.
def create(movies, genre, movie):
	if genre in movies:                #
		movies[genre].append(movie)
	else:
		movies[genre] = [movie]
	print(f"Added {movie} to {genre} movies.")
	

# It defines the name of the function read, that takes one parameter movies and iterating over movies dictionary from the main functions:
def read(movies):
	for genre, movie_list in movies.items():
		print(f"{genre} movies: {', '.join(movie_list)}")

#It define the function named update that takes four parameters: movies, genre, old_movies, new_movies
def update(movies, genre, old_movie, new_movie):
	#Checking Genre Existence in movies:
	if genre in movies:
		for i, movie in enumerate(movies[genre]):
			if old_movie in movie:
				movies[genre][i] = new_movie
				print(f"Updated {old_movie} to {new_movie} in {genre} movies.")
				return
	print(f"{old_movie} not found in {genre} movies.")


#It defines a function named delete that takes three parameters: moveis, genre, movie_title
def delete(movies, genre, movie_title):
	if genre in movies:
		for movie in movies[genre]:
			if movie_title in movie:
				movies[genre].remove(movie)
				print(f"Deleted {movie_title} from {genre} movies.")
				return
	print(f"{movie_title} not found in {genre} movies.")


#Calculates and prints statistical information (mean, median, best, worst durations)
def stats_duration(movies):
	for genre, movie_list in movies.items():
		print(f"Stats for {genre} movies:")
		durations = []
		for movie in movie_list:
			title, runtime = movie.split(', ')
			durations.append(float(runtime))  # Convert runtime to float for accurate calculations
			print(f"{title}: duration {runtime}")
		
		# Calculate and print mean, median, best, and worst durations
		if durations:
			mean_duration = sum(durations) / len(durations)
			median_duration = sorted(durations)[len(durations) // 2]
			best_duration = max(durations)
			worst_duration = min(durations)
			
			print(f"Mean duration: {mean_duration:.2f} hours")
			print(f"Median duration: {median_duration:.2f} hours")
			print(f"Best duration: {best_duration:.2f} hours")
			print(f"Worst duration: {worst_duration:.2f} hours")
			

#To randomly select and print one movie from each genre in the movies dictionary.
def list_random(movies):
	for genre, movie_list in movies.items():
		random_movie = random.choice(movie_list)
		print(f"Random movie from {genre}: {random_movie}")


#To sort and print movies within each genre based on their runtime in ascending order.
def sorted_by_rate(movies):
	for genre, movie_list in movies.items():
		print(f"Sorted movies by runtime for {genre}:")
		sorted_movies = sorted(movie_list, key=lambda x: float(x.split(', ')[1]))
		for movie in sorted_movies:
			print(movie)


#To search for a specific movie title (movie_title) within the movies dictionary and print its details if found.
def search_movie(movies, movie_title):
	found = False
	for genre, movie_list in movies.items():
		for movie in movie_list:
			if movie_title in movie:
				print(f"Found {movie_title} in {genre}: {movie}")
				found = True
	if not found:
		print(f"{movie_title} not found in any genre.")


#To add a predefined movie to a specified genre in the movies dictionary based on a given choice (1 or otherwise).
def enter_choice(movies, genre, choice):
	if genre in movies:
		if choice == "1":
			movies[genre].append("Wingers, 1.36")  # Adjusted duration format for consistency
		else:
			movies[genre].append("Brazil, 2.12")  # Adjusted duration format for consistency
		print(f"Added movie to {genre} based on choice {choice}.")
	else:
		print(f"No movies found in {genre} genre.")
		
		

#function allows interactive management of a movie database stored in the movies dictionary. It provides options to
# list, add, delete, update movies, display stats, select random movies, search movies, sort by rating, and exit the
# program based on user input.
def menu():
	movies = {
		"Action": [
			'Die Hard, 2.12', 'Raiders of the Lost Ark, 1.55', 'Hard Boiled, 2.8', 'Mad Max 2, 1.36'
		],
		"Comedy": [
			'Sister Act, 1.40', 'Brazil, 2.12', 'Wingers, 1.36'
		],
		"Sci-Fi": [
			'2001: A Space Odyssey, 2.29', 'Blade Runner, 1.57', 'Alien, 1.57'
		]
	}
	
	while True:
		print("\nMenu:")
		print("1. List movies")
		print("2. Add movie")
		print("3. Delete movie")
		print("4. Update movie")
		print("5. Stats")
		print("6. Random movie")
		print("7. Search movie")
		print("8. Movies sorted by rating")
		print("9. Exit")
		
		choice = input("\nEnter choice (1-9): ")
		
		if choice == "1":
			read(movies)
		elif choice == "2":
			genre = input("Enter genre: ")
			movie = input("Enter movie title and duration (e.g., Die Hard, 2.12): ")
			create(movies, genre, movie)
		elif choice == "3":
			genre = input("Enter genre: ")
			movie_title = input("Enter movie title to delete: ")
			delete(movies, genre, movie_title)
		elif choice == "4":
			genre = input("Enter genre: ")
			old_movie = input("Enter movie title to update: ")
			new_movie = input("Enter new movie title and duration (e.g., The King of Comedy, 2.9): ")
			update(movies, genre, old_movie, new_movie)
		elif choice == "5":
			stats_duration(movies)
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
