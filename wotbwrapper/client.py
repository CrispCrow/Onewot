from .user import User


class WotbClient:
    def __init__(self, application_id: str) -> None:
        self.application_id = application_id
    
    def get_user(username: str) -> User:
        ...