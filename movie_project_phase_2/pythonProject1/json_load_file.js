def load_from_file(filename='movies.json'):
    global movies
    try:
        with open(filename, 'r') as f:
            movies = json.load(f)
        print(f"Movies loaded from {filename}")
    except FileNotFoundError:
        print(f"No existing database found. A new one will be created.")
