from project.resources.user import User
from faker import Faker

fake = Faker()


class DataGenerator:

    @staticmethod
    def generate_random_user():
        yield User(
            full_name=fake.name(),
            email=fake.email(),
            current_address=fake.address(),
            permanent_address=fake.address()
        )

    @staticmethod
    def get_random_user():
        return next(DataGenerator.generate_random_user())
