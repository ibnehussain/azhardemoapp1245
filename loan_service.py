class LoanService:
    def calculate_fine(self, days_late):
        if days_late <= 0:
            return 0
        if days_late <= 5:
            return days_late * 10
        return days_late * 20

    def can_borrow(self, active_loans):
        return active_loans < 5
