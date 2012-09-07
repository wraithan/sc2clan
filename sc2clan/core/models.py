from django.db import models

from model_utils import Choices


class Profile(models.Model):
    user = models.ForeignKey('auth.User')
    working_on = models.TextField(default='', blank=True)


class Account(models.Model):
    profile = models.ForeignKey('core.Profile', related_name='accounts')
    starcraft_username = models.CharField(max_length=255)
    starcraft_number = models.PositiveIntegerField(default=None, blank=True,
                                                   null=True)
    real_id = models.EmailField(max_length=254, default='', blank=True,
                                null=True)
    primary = models.BooleanField(default=True)

    @property
    def get_starcraft_number_display(self):
        if self.starcraft_number:
            return '+%03d' % self.starcraft_number
        else:
            return ''


class Race(models.Model):
    NAME = Choices('Protoss', 'Terran', 'Zerg', 'Random')
    LEAGUE = Choices(('bronze', 'Bronze League'),
                    ('silver', 'Silver League'),
                    ('gold', 'Gold League'),
                    ('platinum', 'Platinum League'),
                    ('diamond', 'Diamond League'),
                    ('master', 'Master League'),
                    ('grandmaster', 'Grandmaster League'))
    TYPE = Choices(('1v1', 'v1', '1v1'),
                  ('2v2 random', 'v2r', '2v2 random'),
                  ('2v2 team', 'v2t', '2v2 team'),
                  ('3v3 random', 'v3r', '3v3 random'),
                  ('3v3 team', 'v3t', '3v3 team'),
                  ('4v4 random', 'v4r', '4v4 random'),
                  ('4v4 team', 'v4t', '4v4 team'))
    profile = models.ForeignKey('core.Profile', related_name='races')
    name = models.CharField(max_length=8,
                            choices=NAME)
    league = models.CharField(max_length=12,
                              choices=LEAGUE)
    game_type = models.CharField(max_length=12,
                                 choices=TYPE)
