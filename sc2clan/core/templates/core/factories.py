import factory
from models import User


class RaceFactory(factory.Factory):
    name = 'protoss'


class LeagueFactory(factory.Factory):
    name = 'gold'
    game_type = '1v1'

class UserFactory(factory.Factory):
    FACTORY_FOR = Profile

    name = 'John Doe'
    starcraft_id = 'JohnDoezer'
    starcraft_id_number = 239
    real_id = 'john@doe.com'
    working_on = 'John Doezing everyone I come up against.'

    @factory.post_generation()
    def races(self, obj, create, extracted, **kwargs):
        