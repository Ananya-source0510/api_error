class AppException(Exception):
    def __init__(self, message: str, status_code: int = 400, details: dict | None = None):
        self.message = message
        self.status_code = status_code
        self.details = details


class ResourceNotFoundException(AppException):
    def __init__(self, resource: str):
        super().__init__(
            message=f"{resource} not found",
            status_code=404
        )


class UnauthorizedException(AppException):
    def __init__(self):
        super().__init__(
            message="Unauthorized access",
            status_code=401
        )
