import json
import random

from src.singletons.appsettings import appsettings

class symbols_repository:
    """This repostiory is responsible for managing the symbols file."""
    
    def __init__(self, settings: appsettings):
        self.connection_string = settings.symbols_connection_string

    def get_random(self, num: int) -> list[str]:
        """
        Gets a specified amount of random symbols.

        num (int): The number of symbols to randomly select.
        """

        all_symbols = self.get_all()

        return random.sample(all_symbols, num)


    def get_all(self) -> list[str]:
        """Gets all the symbols as a list of strings."""

        symbols: dict[str, list[str]] = self.__open__()

        symbols_list: list[str] = []

        for key in symbols:
            for symbol in symbols[key]:
                symbols_list.append(symbol)
        
        return symbols_list
    
    def __open__(self) -> dict[str, list[str]]:
        """Opens the symbols file as a dictionary."""

        with open(self.connection_string, "r") as f:
            return json.load(f)