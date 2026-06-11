class LibraryError(Exception):
    pass

# Authentication
class AuthenticationError(LibraryError):
    pass

class AuthorizationError(LibraryError):
    pass

# Books
class BookNotFoundError(LibraryError):
    pass

class BookOutOfStockError(LibraryError):
    pass

class DuplicateBookError(LibraryError):
    pass

# Borrowing
class DuplicateIssuanceError(LibraryError):
    pass

class RecordNotFoundError(LibraryError):
    pass

class MaxBooksExceededError(LibraryError):
    pass

# Input
class ValidationError(LibraryError):
    pass

# Infrastructure
class DatabaseError(LibraryError):
    pass

class ConfigurationError(LibraryError):
    pass