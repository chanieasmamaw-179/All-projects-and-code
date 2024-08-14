import random
def create_read_update_delete():
	movies = {
		"Action": [
			'Die Hard, 2h 12m', 'Raiders of the Lost Ark, 1h 55m', 'Hard Boiled, 2h 8m', 'Mad Max 2, 1h 36m'
		],
		"Comedy": [
			'Sister Act, 1h 40m', 'Brazil, 2h 12m', 'Wingers, 1h 36m'
		],
		"Sci-Fi": [
			'2001: A Space Odyssey, 2h 29m', 'Blade Runner, 1h 57m', 'Alien, 1h 57m'
		]
	}
	
	def create(genre, movie):
		if genre in movies:
			movies[genre].append(movie)
		else:
			movies[genre] = [movie]
		print(f"Added {movie} to {genre} movies.")
	
	def read():
		for genre, movie_list in movies.items():
			print(f"{genre} movies: {', '.join(movie_list)}")
	
	def update(genre, old_movie, new_movie):
		if genre in movies:
			for i, movie in enumerate(movies[genre]):
				if old_movie in movie:
					movies[genre][i] = new_movie
					print(f"Updated {old_movie} to {new_movie} in {genre} movies.")
					return
		print(f"{old_movie} not found in {genre} movies.")
	
	def delete(genre, movie_title):
		if genre in movies:
			for movie in movies[genre]:
				if movie_title in movie:
					movies[genre].remove(movie)
					print(f"Deleted {movie_title} from {genre} movies.")
					return
		print(f"{movie_title} not found in {genre} movies.")
	
	def stats_duration():
		for genre, movie_list in movies.items():
			print(f"Stats for {genre} movies:")
			for movie in movie_list:
				title, runtime = movie.split(', ')
				print(f"{title}: duration {runtime}")
	
	def list_random():
		for genre, movie_list in movies.items():
			random_movie = random.choice(movie_list)
			print(f"Random movie from {genre}: {random_movie}")
	
	def sorted_by_rate():
		for genre, movie_list in movies.items():
			print(f"Sorted movies by runtime for {genre}:")
			sorted_movies = sorted(movie_list, key=lambda x: x.split(', ')[1])
			for movie in sorted_movies:
				print(movie)
	
	def search_movie(movie_title):
		found = False
		for genre, movie_list in movies.items():
			for movie in movie_list:
				if movie_title in movie:
					print(f"Found {movie_title} in {genre}: {movie}")
					found = True
		if not found:
			print(f"{movie_title} not found in any genre.")
	
	def enter_choice(genre, choice):
		if genre in movies:
			if choice == "1":
				movies[genre].append("Wingers, 1h 36m")
			else:
				movies[genre].append("Brazil, 2h 12m")
			print(f"Added movie to {genre} based on choice {choice}.")
		else:
			print(f"No movies found in {genre} genre.")
	
	# Example operations:
	print("List of movies:")
	read()
	
	print("\nPerforming CRUD operations:")
	create("Action", "Mad Max 3, 1h 45m")
	update("Comedy", "Sister Act", "The King of Comedy, 2h 9m")
	delete("Sci-Fi", "2001: A Space Odyssey")
	
	print("\nStats:")
	stats_duration()
	
	print("\nRandom Movie:")
	list_random()
	
	print("\nSorted by Runtime:")
	sorted_by_rate()
	
	print("\nSearch Movie:")
	search_movie("Alien")
	
	print("\nEnter Choice:")
	enter_choice("Comedy", "2")
	
	print("\nUpdated movies:")
	read()

create_read_update_delete()
