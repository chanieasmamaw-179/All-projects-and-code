
import random
import numpy as np
import matplotlib.pyplot as plt

def create_read_update_delete():
    movies = {
        "Action": [
            ('Die Hard', 9.5), ('Mad Max 2', 8.1), ('Die Hard', 2.12), ('Raiders of the Lost Ark', 1.55), ('Hard Boiled', 2.8), ('Mad Max', 1.36)
        ],
        "Comedy": [
            ('Sister Act', 6.3), ('Brazil', 8.8), ('Wingers', 1.36)
        ],
        "Sci-Fi": [
            ('2001: A Space Odyssey', 8.3), ('Blade Runner', 8.7), ('Alien', 1.57)
        ]
    }

    def create(genre, movie, rating):
        if genre in movies:
            movies[genre].append((movie, rating))
        else:
            movies[genre] = [(movie, rating)]
        print(f"Added {movie} to {genre} movies with rating {rating}.")

    def read():
        for genre, movie_list in movies.items():
            print(f"{genre} movies:")
            for movie, rating in movie_list:
                print(f" - {movie}, Rating: {rating}")

    def update(genre, old_movie, new_movie, new_rating):
        if genre in movies:
            for i, (movie, rating) in enumerate(movies[genre]):
                if old_movie == movie:
                    movies[genre][i] = (new_movie, new_rating)
                    print(f"Updated {old_movie} to {new_movie} with rating {new_rating} in {genre} movies.")
                    return
        print(f"{old_movie} not found in {genre} movies.")

    def delete(genre, movie_title):
        if genre in movies:
            for movie in movies[genre]:
                if movie_title == movie[0]:
                    movies[genre].remove(movie)
                    print(f"Deleted {movie_title} from {genre} movies.")
                    return
        print(f"{movie_title} not found in {genre} movies.")

    def stats():
        for genre, movie_list in movies.items():
            print(f"Stats for {genre} movies:")
            for movie, rating in movie_list:
                print(f" - {movie}: Rating {rating}")

    def list_random():
        all_movies = [(movie, genre) for genre in movies for movie in movies[genre]]
        random_movie, genre = random.choice(all_movies)
        print(f"Random movie: {random_movie[0]} from {genre} genre with rating {random_movie[1]}")

    def sorted_by_rating():
        for genre, movie_list in movies.items():
            print(f"Sorted movies by rating for {genre}:")
            sorted_movies = sorted(movie_list, key=lambda x: x[1], reverse=True)
            for movie, rating in sorted_movies:
                print(f" - {movie}, Rating: {rating}")

    def search_movie(movie_title):
        found = False
        for genre, movie_list in movies.items():
            for movie, rating in movie_list:
                if movie_title.lower() in movie.lower():
                    print(f"Found {movie_title} in {genre} genre: {movie}, Rating: {rating}")
                    found = True
        if not found:
            print(f"{movie_title} not found in any genre.")

    def print_menu():
        print("\n********** My Movies Database **********\n")
        print("Menu:")
        print("1. List movies")
        print("2. Add movie")
        print("3. Delete movie")
        print("4. Update movie")
        print("5. Stats")
        print("6. Random movie")
        print("7. Search movie")
        print("8. Movies sorted by rating")
        print("9. Show histogram of movie ratings")
        print("10. Exit")

    def show_histogram():
        ratings = [rating for genre in movies.values() for movie, rating in genre]
        plt.hist(ratings, bins=10, edgecolor='black')
        plt.xlabel('Ratings')
        plt.ylabel('Frequency')
        plt.title('Histogram of Movie Ratings')
        plt.show()

    def main():
        while True:
            print_menu()
            choice = input("Enter your choice (1-10): ")
            if choice == "1":
                read()
            elif choice == "2":
                genre = input("Enter genre: ")
                movie = input("Enter movie title: ")
                rating = float(input("Enter movie rating: "))
                create(genre, movie, rating)
            elif choice == "3":
                genre = input("Enter genre: ")
                movie = input("Enter movie title to delete: ")
                delete(genre, movie)
            elif choice == "4":
                genre = input("Enter genre: ")
                old_movie = input("Enter current movie title: ")
                new_movie = input("Enter new movie title: ")
                new_rating = float(input("Enter new movie rating: "))
                update(genre, old_movie, new_movie, new_rating)
            elif choice == "5":
                stats()
            elif choice == "6":
                list_random()
            elif choice == "7":
                movie_title = input("Enter movie title to search: ")
                search_movie(movie_title)
            elif choice == "8":
                sorted_by_rating()
            elif choice == "9":
                show_histogram()
            elif choice == "10":
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")

    main()

create_read_update_delete()
