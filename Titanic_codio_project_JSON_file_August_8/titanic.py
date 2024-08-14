import json
import cmd
from collections import Counter


class ShipCLI(cmd.Cmd):
	intro = "Welcome to the Ships CLI! Enter 'help' to view available commands."
	prompt = "(ships-cli) "
	
	def __init__(self, filename):
		super().__init__()
		self.filename = filename
		self.ships = self.load_data(filename)
	
	def load_data(self, filename):
		"""Load JSON data from a file."""
		with open(filename, 'r') as file:
			return json.load(file)['data']
	
	def do_count(self, arg):
		"""Print the number of ships"""
		number_of_ships = len(self.ships)
		print(f"Total number of ships: {number_of_ships}")
	
	def do_names(self, arg):
		"""Print the names of all ships"""
		print("Ship names:")
		for ship in self.ships:
			print(ship['SHIPNAME'])
	
	def do_countries(self, arg):
		"""Print the countries of all ships"""
		print("Ship countries:")
		for ship in self.ships:
			print(ship['COUNTRY'])
	
	def do_unique_countries(self, arg):
		"""Print unique countries of ships"""
		unique_countries_set = {ship['COUNTRY'] for ship in self.ships}
		print("Unique ship countries:")
		for country in unique_countries_set:
			print(country)
	
	def do_top_countries(self, arg):
		"""Print the top 5 countries with the most ships"""
		country_counter = Counter(ship['COUNTRY'] for ship in self.ships)
		top_5_countries = country_counter.most_common(5)
		print("Top 5 countries with the most ships:")
		for country, count in top_5_countries:
			print(f"{country}: {count}")
	
	def do_exit(self, arg):
		"""Exit the CLI"""
		print("Goodbye!")
		return True
	
	def do_help(self, arg):
		"""List available commands with 'help' or detailed help with 'help cmd'"""
		super().do_help(arg)


if __name__ == "__main__":
	import argparse
	
	parser = argparse.ArgumentParser(description="Ship data exploration CLI")
	parser.add_argument('filename', type=str, help='The JSON file containing ship data')
	args = parser.parse_args()
	
	ShipCLI(args.filename).cmdloop()
