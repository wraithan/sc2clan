from django.db import models


class Profile(models.Model):
    user = models.ForeignKey('auth.User')
    starcraft_id = models.CharField(max_length=255)
    starcraft_id_number = models.PositiveIntegerField()
    real_id = models.EmailField(max_length=254)
    races = models.ManyToManyField('core.Race')
    leagues = models.ManyToManyField('core.League')
    working_on = models.TextField()


class Race(models.Model):
    name = models.CharField(max_length=8,
                            choices=(('protoss','Protoss'),
                                     ('terran','Terran'),
                                     ('zerg', 'Zerg'),
                                     ('random','Random')))


class League(models.Model):
    name = models.CharField(max_length=12,
                            choices=(('bronze','Bronze League'),
                                     ('silver','Silver League'),
                                     ('gold','Gold League'),
                                     ('platinum','Platinum League'),
                                     ('diamond','Diamond League'),
                                     ('master','Master League'),
                                     ('grandmaster','Grandmaster League'),))
    game_type = models.CharField(max_length=12,
                                 choices=(('1v1','1v1'),
                                          ('2v2 random','2v2 random'),
                                          ('2v2 team','2v2 team'),
                                          ('3v3 random','3v3 random'),
                                          ('3v3 team','3v3 team'),
                                          ('4v4 random','4v4 random'),
                                          ('4v4 team','4v4 team'),))
