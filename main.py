

from src.repositories.symbols_repository import symbols_repository
from src.singletons.appsettings import appsettings


def main():
    settings = appsettings()
    symbols = symbols_repository(settings)

    [print(symbol, end=" ") for symbol in symbols.get_all()]


if __name__ == "__main__":
    main()