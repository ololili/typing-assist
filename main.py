from src.services.test_service import test_service
from src.repositories.symbols_repository import symbols_repository
from src.singletons.appsettings import appsettings


def main():
    settings = appsettings()
    symbols = symbols_repository(settings)
    tester = test_service(symbols)

    tester.repeated_tests(5, 3)


if __name__ == "__main__":
    main()