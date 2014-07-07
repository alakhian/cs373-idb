from django.db import models

# Models for the NBA app

class Team(models.Model) :
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    #logo
    #yearsactive
    #years with results of season
    #current coach
    #current gm
    #current owner
    #current roster (possible links to player models)

class Player(models.Model) :
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=2)
    education = models.CharField(max_length=200)
    yearsExp = models.IntegerField(default=0)
    #separate stats or a list of all of them?
    #teams played for and years
    #awards
    #years went to playoffs (playoff model)

class Year(models.Model) :
    #all nba 1st team (players)
    #all nba defensive (players)
    #finals mvp (player)
    #champion (team)
