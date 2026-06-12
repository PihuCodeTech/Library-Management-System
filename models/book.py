from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Book:
    book_id:      int
    title:        str
    author:       str
    genre:        Optional[str]      = None
    stock:        int                = 0
    total_copies: int                = 0
    isbn:         Optional[str]      = None
    created_at:   Optional[datetime] = None
    updated_at:   Optional[datetime] = None

    @property
    def is_available(self) -> bool:
        return self.stock > 0

    @property
    def issued_count(self) -> int:
        return max(0, self.total_copies - self.stock)

    def to_dict(self) -> dict:
        return {
            "book_id":      self.book_id,
            "isbn":         self.isbn,
            "title":        self.title,
            "author":       self.author,
            "genre":        self.genre or "Uncategorized",
            "stock":        self.stock,
            "total_copies": self.total_copies,
            "is_available": self.is_available,
        }

    def __str__(self) -> str:
        return f"[{self.book_id}] {self.title} — {self.author}"