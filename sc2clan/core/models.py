from django.db import models


class Profile(models.Model):
    user = models.ForeignKey('auth.User')
    races = models.ManyToManyField('core.Race')
    starcraft_username = models.CharField(max_length=255)
    starcraft_number = models.PositiveIntegerField(default=0)
    real_id = models.EmailField(max_length=254, blank=True, default='')
    working_on = models.TextField(blank=True, default='')

    @property
    def starcraft_number_display(self):
        if self.starcraft_number:
            return '+%03d' % self.starcraft_number
        else:
            return ''


class Race(models.Model):
    name = models.CharField(max_length=8,
                            choices=(('protoss', 'Protoss'),
                                     ('terran', 'Terran'),
                                     ('zerg', 'Zerg'),
                                     ('random', 'Random')))
    league = models.CharField(max_length=12,
                              choices=(('bronze', 'Bronze League'),
                                       ('silver', 'Silver League'),
                                       ('gold', 'Gold League'),
                                       ('platinum', 'Platinum League'),
                                       ('diamond', 'Diamond League'),
                                       ('master', 'Master League'),
                                       ('grandmaster', 'Grandmaster League')))
    game_type = models.CharField(max_length=12,
                                 choices=(('1v1', '1v1'),
                                          ('2v2 random', '2v2 random'),
                                          ('2v2 team', '2v2 team'),
                                          ('3v3 random', '3v3 random'),
                                          ('3v3 team', '3v3 team'),
                                          ('4v4 random', '4v4 random'),
                                          ('4v4 team', '4v4 team')))
