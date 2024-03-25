from dotenv import load_dotenv
import os
import starkbank


class StarkbankAuth:
    load_dotenv('../.env')
    private_key = os.getenv('PRIVATE_KEY')
    project_id = os.getenv('PROJECT_ID')
    type_of_endpoint = os.getenv('TYPE_OF_ENVIRONMENT')

    @staticmethod
    def auth():
        user = starkbank.Project(environment=StarkbankAuth.type_of_endpoint,
                                 id=StarkbankAuth.project_id,
                                 private_key=StarkbankAuth.private_key)
        starkbank.user = user
        return starkbank.user
