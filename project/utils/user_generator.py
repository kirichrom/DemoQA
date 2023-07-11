from project.resources.user import User
from faker import Faker

fake = Faker()


class UserGenerator:

    @staticmethod
    def generate_random_user():
        yield User(
            full_name=fake.name(),
            email=fake.email(),
            current_address=fake.address(),
            permanent_address=fake.address()
        )

    @staticmethod
    def get_random_user() -> User:
        return next(UserGenerator.generate_random_user())

    @staticmethod
    def get_users_list(number: int) -> list:
        return [UserGenerator.get_random_user() for _ in range(number)]
