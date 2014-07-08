from django.db import models

# Models for the NBA app

class Team(models.Model) :
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=30)
    coach = models.CharField(max_length=30)
    gm = models.CharField(max_length=30)
    owner = models.CharField(max_length=30)
    #twitter
    #logo
    #years with results of season (record, playoff recap, mvp awards)

class Player(models.Model) :
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=2)
    education = models.CharField(max_length=200)
    yearsExp = models.IntegerField(default=0)
    #stats by year with team played for, gp, gs, min, fg%, ft%, reb, ast, blk, stl, pts
    #awards for MVP, Finals MVP, all-NBA 1st team, all-defensive 1st team
    #twitter
    #photo

class Year(models.Model) :
    #year
    #all nba 1st team (players)
    #all nba defensive (players)
    #finals mvp (player)
    #champion (team)
    #finals logo
    #finals recap

