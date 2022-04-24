class VacationDaysShortageError(Exception):
    """ Custom error that is raised when not enough vacation days is available. """
    def __init__(self, requested_days: int, remaining_days: int, message: str):
        self.requested_days = requested_days
        self.remaining_days = remaining_days
        self.message = message
        super().__init__(message)