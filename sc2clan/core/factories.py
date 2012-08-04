import factory
from sc2clan.core.models import Profile


class RaceFactory(factory.Factory):
    name = 'protoss'
    league = 'gold'
    game_type = '1v1'


class UserFactory(factory.Factory):
    FACTORY_FOR = Profile

    name = 'John Doe'
    starcraft_id = 'JohnDoezer'
    starcraft_id_number = 239
    real_id = 'john@doe.com'
    working_on = 'John Doezing everyone I come up against.'
