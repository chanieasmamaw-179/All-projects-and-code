def main():
    """Command-Line Interface (CLI) for interacting with the movie database."""
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

    # Create table if it doesn't exist
    create_table()

    # Execute the command based on the user's input
    if args.command == 'list':
        load_movies()

    elif args.command == 'add':
        if args.title and args.rating and args.genre and args.year:
            additional_properties = {}
            if args.properties:
                for prop in args.properties:
                    key, value = prop.split('=')
                    additional_properties[key.strip()] = value.strip()
            add_movie(args.title, args.rating, args.genre, args.year, **additional_properties)
        else:
            print(Fore.RED + "Error: Title, rating, genre, and year are required for adding a movie.")

    elif args.command == 'delete':
        if args.title:
            delete_movie(args.title)
        else:
            print(Fore.RED + "Error: Title is required for deleting a movie.")

    elif args.command == 'update':
        if args.old_title and args.title and args.rating and args.genre and args.year:
            additional_properties = {}
            if args.properties:
                for prop in args.properties:
                    key, value = prop.split('=')
                    additional_properties[key.strip()] = value.strip()
            update_movie(args.old_title, args.title, args.rating, args.genre, args.year, **additional_properties)
        else:
            print(Fore.RED + "Error: Old title, new title, rating, genre, and year are required for updating a movie.")

    elif args.command == 'stats':
        stats_rating()

    elif args.command == 'random':
        list_random()

    elif args.command == 'search':
        if args.title:
            search_movie(args.title)
        else:
            print(Fore.RED + "Error: Title is required for searching a movie.")

    elif args.command == 'sort':
        sorted_by_rate()

    else:
        print(Fore.RED + "Unknown command.")
