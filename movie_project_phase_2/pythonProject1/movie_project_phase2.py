import random
import statistics as stat
import matplotlib.pyplot as plt
import colorama
from colorama import Fore, Style
import argparse
from movie_storage import get_movies, add_movie, delete_movie, update_movie


def read_movie(movies):
    """Print all movies in the dictionary."""
    try:
        if not movies:
            print("No movies in the list.")
        else:
            for movie in movies.values():
                properties = ", ".join(
                    [f"{key}: {value}" for key, value in movie.items()]
                )
                print(f"{properties}")
    except Exception as e:
        print(Fore.RED + f"Error reading movies: {e}" + Style.RESET_ALL)


def stats_rating(movies):
    """Calculate and print movie statistics."""
    try:
        if movies:
            ratings = [movie["rating"] for movie in movies.values()]
            average_rating = stat.mean(ratings)
            median_rating = stat.median(ratings)
            best_movie = max(movies.values(), key=lambda x: x["rating"])
            worst_movie = min(movies.values(), key=lambda x: x["rating"])
            print(f"Average rating: {average_rating:.2f}")
            print(f"Median rating: {median_rating:.2f}")
            print(
                f"Best rating: {best_movie['rating']} ({best_movie['title']} - {best_movie['year']})"
            )
            print(
                f"Worst rating: {worst_movie['rating']} ({worst_movie['title']} - {worst_movie['year']})"
            )

            # Plotting the ratings of movies
            titles = [movie["title"] for movie in movies.values()]
            plt.figure(figsize=(6, 4))
            plt.bar(titles, ratings, color="black")
            plt.xlabel("Movies")
            plt.ylabel("Ratings")
            plt.title("Ratings of Movies")
            plt.xticks(rotation=90)
            plt.show()
        else:
            print("No statistics to calculate.")
    except Exception as e:
        print(Fore.RED + f"Error calculating statistics: {e}" + Style.RESET_ALL)


def list_random(movies):
    """Print a random movie."""
    try:
        if movies:
            random_movie = random.choice(list(movies.values()))
            print(
                f"Random movie: {random_movie['title']} ({random_movie['genre']}, {random_movie['year']}): {random_movie['rating']} rating"
            )
        else:
            print("No movies available.")
    except Exception as e:
        print(Fore.RED + f"Error selecting random movie: {e}" + Style.RESET_ALL)


def sorted_by_rate(movies):
    """Print movies sorted by rating."""
    try:
        sorted_movies = sorted(movies.values(), key=lambda x: x["rating"])
        for movie in sorted_movies:
            print(
                f"Sorted movie: {movie['title']} ({movie['genre']}, {movie['year']}): {movie['rating']} rating"
            )
    except Exception as e:
        print(Fore.RED + f"Error sorting movies: {e}" + Style.RESET_ALL)


def search_movie(movies, movie_title):
    """Search for a movie by title."""
    try:
        movie_titles = list(movies.keys())
        search_movie_lower = movie_title.lower()
        # This partial fuzzy string ratio finds some of the strings match and retrieves from the database
        best_match, score = process.extractOne(
            search_movie_lower, movie_titles, scorer=fuzz.partial_ratio
        )

        if score >= 50:  # Threshold for a good match
            movie = movies[best_match]
            properties = ", ".join([f"{key}: {value}" for key, value in movie.items()])
            print(f"Found {properties} (Score: {score})")
        else:
            print(Fore.RED + f"Movie {movie_title} not found." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error searching for movie: {e}" + Style.RESET_ALL)


# Command-Line Interface (CLI)
def main():
    try:
        movies = {
            "the shawshank redemption": {
                "title": "The Shawshank Redemption",
                "rating": 9.3,
                "genre": "Drama",
            },
            "pulp fiction": {"title": "Pulp Fiction", "rating": 8.9, "genre": "Crime"},
            "the godfather": {
                "title": "The Godfather",
                "rating": 9.2,
                "genre": "Crime",
            },
            "the dark knight": {
                "title": "The Dark Knight",
                "rating": 9.0,
                "genre": "Action",
            },
            "forrest gump": {"title": "Forrest Gump", "rating": 8.8, "genre": "Drama"},
            "inception": {"title": "Inception", "rating": 8.8, "genre": "Sci-Fi"},
            "fight club": {"title": "Fight Club", "rating": 8.8, "genre": "Drama"},
            "the matrix": {"title": "The Matrix", "rating": 8.7, "genre": "Sci-Fi"},
            "goodfellas": {"title": "Goodfellas", "rating": 8.7, "genre": "Crime"},
            "interstellar": {"title": "Interstellar", "rating": 8.6, "genre": "Sci-Fi"},
        }

        parser = argparse.ArgumentParser(description="Movie Database CLI")

        # Define the arguments for the CLI
        parser.add_argument(
            "command",
            choices=[
                "list",
                "add",
                "delete",
                "update",
                "stats",
                "random",
                "search",
                "sort",
            ],
            help="Command to execute",
        )

        # Arguments for adding or updating a movie
        parser.add_argument("--title", help="Movie title")
        parser.add_argument("--rating", type=float, help="Movie rating")
        parser.add_argument("--genre", help="Movie genre")
        parser.add_argument("--year", type=int, help="Year of release")
        parser.add_argument(
            "--properties", nargs="*", help="Additional properties in key=value format"
        )

        # Arguments for searching, updating, or deleting a movie
        parser.add_argument(
            "--old-title", help="Current title of the movie (for updating)"
        )

        # Parse the arguments
        args = parser.parse_args()

        # Load movie database
        movies = get_movies()

        # Execute the command based on the user's input
        if args.command == "list":
            read_movie(movies)

        elif args.command == "add":
            if args.title and args.rating and args.genre and args.year:
                additional_properties = {}
                if args.properties:
                    for prop in args.properties:
                        key, value = prop.split("=")
                        additional_properties[key.strip()] = value.strip()
                add_movie(
                    movies,
                    args.title,
                    args.rating,
                    args.genre,
                    args.year,
                    **additional_properties,
                )
            else:
                print(
                    Fore.RED
                    + "Error: Title, rating, genre, and year are required for adding a movie."
                    + Style.RESET_ALL
                )

        elif args.command == "delete":
            if args.title:
                delete_movie(movies, args.title)
            else:
                print(
                    Fore.RED
                    + "Error: Title is required for deleting a movie."
                    + Style.RESET_ALL
                )

        elif args.command == "update":
            if (
                args.old_title
                and args.title
                and args.rating
                and args.genre
                and args.year
            ):
                additional_properties = {}
                if args.properties:
                    for prop in args.properties:
                        key, value = prop.split("=")
                        additional_properties[key.strip()] = value.strip()
                update_movie(
                    movies,
                    args.old_title,
                    args.title,
                    args.rating,
                    args.genre,
                    args.year,
                    **additional_properties,
                )
            else:
                print(
                    Fore.RED
                    + "Error: Old title, new title, rating, genre, and year are required for updating a movie."
                    + Style.RESET_ALL
                )

        elif args.command == "stats":
            stats_rating(movies)

        elif args.command == "random":
            list_random(movies)

        elif args.command == "search":
            if args.title:
                search_movie(movies, args.title)
            else:
                print(
                    Fore.RED
                    + "Error: Title is required for searching a movie."
                    + Style.RESET_ALL
                )

        elif args.command == "sort":
            sorted_by_rate(movies)

        else:
            print(Fore.RED + "Unknown command." + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)


# Run the CLI
if __name__ == "__main__":
    main()
