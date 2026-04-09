import json

class appsettings:
    """This class holds settings that are used across the application."""

    symbols_connection_string: str
    """The connection string that points to the symbols file."""

    def __init__(self):
        with open("appsettings.json", "r") as f:
            settings: dict[str, str] = json.load(f)

            self.symbols_connection_string = settings["symbols_connection_string"]


