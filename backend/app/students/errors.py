from app.exceptions import ServerError


class StudentNotFound(ServerError):
    def __init__(
        self, message: str = "invalid session", status_code: int = 404
    ) -> None:
        super().__init__(message=message, status_code=status_code)


class StudentAlreadyExists(ServerError):
    def __init__(
        self, message: str = "Student already exists", status_code: int = 403
    ) -> None:
        super().__init__(message=message, status_code=status_code)
