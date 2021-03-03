from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        app_label = 'tournament'


class Coach(models.Model):
    name = models.CharField(max_length=48)
    experience = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        app_label = 'tournament'
