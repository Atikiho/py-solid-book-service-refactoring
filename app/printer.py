from abc import ABC, abstractmethod


class Printer(ABC):
    def __init__(self, book):
        self.book = book

    @abstractmethod
    def print_book(self) -> None:
        pass


class ConsolePrinter(Printer):
    def print_book(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)


class ReversePrinter(Printer):
    def print_book(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content[::-1])
