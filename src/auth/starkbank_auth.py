import starkbank
from src.config import get_settings


class StarkbankAuth:
    """
    Class responsible for starkbank API authentication
    """
    @staticmethod
    def auth():
        try:
            user = starkbank.Project(environment=get_settings().type_of_environment,
                                     id=get_settings().project_id,
                                     private_key=get_settings().private_key)
            starkbank.user = user
            return starkbank.user

        except Exception as e:
            print(f"Unexpected error: {e}")
