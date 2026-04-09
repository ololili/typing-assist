from src.repositories.symbols_repository import symbols_repository


class test_service:
    """A service for handling the testing of the user."""
    
    symbols: symbols_repository
    """The repository of the symbols."""

    wrong_symbols: list[str] = []
    """A list containing the symbols that were typed incorrectly last time."""

    def __init__(self, symbols: symbols_repository):
        self.symbols = symbols
    
    def repeated_tests(self, repeats: int, test_length: int) -> None:
        """Perfoms a number of typing tests for the user."""
        for _ in range(repeats):
            self.test_user(test_length)

    def test_user(self, test_length: int) -> None:
        """Perfoms a single typing test for the user."""

        symbols = self.get_symbols(test_length)

        text = self.generate_input_message(symbols)
        result = self.get_result(text)
        self.wrong_symbols = self.verify(user_symbols=result, true_symbols=symbols)


    def get_symbols(self, num: int) -> list[str]:
        """Gets a number of random symbols that are added to the pre-existing wrong symbols list."""

        new_symbols = self.symbols.get_random(max(0, num - len(self.wrong_symbols)))

        symbols = self.wrong_symbols.copy()
        symbols.extend(new_symbols)

        return symbols
    
    @staticmethod
    def verify(user_symbols: list[str], true_symbols: list[str]) -> list[str]:
        """
        Verify a list of user generated symbols against a list of true symbols.

        user_symbols (list[str]): The list of symbols that the user typed.
        true_symbols (list[str]): The list of symbols that the user was supposed to type.

        Returns:
        A list of symbols that the user was supposed to type, but failed to do so accurately.
        """

        wrong_symbols: list[str] = []

        for i in range(len(true_symbols)):
            if true_symbols[i] != user_symbols[i]:
                wrong_symbols.append(true_symbols[i])
        
        return wrong_symbols

    @staticmethod
    def generate_input_message(symbols: list[str]) -> str:
        """
        Generate a message asking the user to type out a list of symbols.

        symbols (list[str]): A list of symbols that the user will be asked to type.

        Returns:
        The completed message.
        """

        starting_text: str = "Please type the following symbols:\n"
        starting_text.join(symbols)
        return starting_text
    
    @staticmethod
    def get_result(message: str) -> list[str]:
        """
        Show a message to the user and get their response.
        
        message (str): The message that will be shown to the user.

        Returns:
        A list of every symbol that the user typed in response to the message.
        """
        
        result_text = input(message)

        result_list: list[str] = [symbol for symbol in result_text]

        return result_list
        