from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional

@dataclass
class BorrowRecord:
    record_id:   int
    book_id:     int
    user_id:     str
    issue_date:  date
    due_date:    date
    return_date: Optional[date]     = None
    fine_amount: float              = 0.0
    created_at:  Optional[datetime] = None

    @property
    def is_returned(self) -> bool:
        return self.return_date is not None

    @property
    def is_active(self) -> bool:
        return self.return_date is None

    @property
    def is_overdue(self) -> bool:
        if self.is_returned:
            return False
        return date.today() > self.due_date

    @property
    def days_overdue(self) -> int:
        if self.is_returned or not self.is_overdue:
            return 0
        return (date.today() - self.due_date).days

    @property
    def status_label(self) -> str:
        if self.is_returned:
            return "Returned"
        if self.is_overdue:
            return f"OVERDUE ({self.days_overdue}d)"
        return "Active"

    def calculate_fine(self, fine_per_day: int) -> int:
        reference = self.return_date if self.is_returned else date.today()
        delay_days = (reference - self.due_date).days
        return max(0, delay_days * fine_per_day)

    def to_dict(self) -> dict:
        return {
            "record_id":    self.record_id,
            "book_id":      self.book_id,
            "user_id":      self.user_id,
            "issue_date":   str(self.issue_date),
            "due_date":     str(self.due_date),
            "return_date":  str(self.return_date) if self.return_date else None,
            "fine_amount":  self.fine_amount,
            "status":       self.status_label,
            "days_overdue": self.days_overdue,
        }

    def __str__(self) -> str:
        return (f"Record #{self.record_id} | "
                f"Book #{self.book_id} | "
                f"{self.user_id} | "
                f"{self.status_label}")