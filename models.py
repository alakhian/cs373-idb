from django.db import models

# Models for the NBA app

class Team(models.Model) :
    name = models.CharField(max_length=20, unique=True)
    location = models.CharField(max_length=30, unique=True)
    coach = models.CharField(max_length=30, unique=True)
    gm = models.CharField(max_length=30, unique=True)
    owner = models.CharField(max_length=30)
    twitter = models.URLField(unique=True)
    logo = models.URLField(unique=True)
    #years with results of season (record, playoff recap, mvp awards)

    def __unicode__(self) :
        return self.name

class Player(models.Model) :
    name = models.CharField(max_length=30, unique=True)
    position = models.CharField(max_length=2)
    education = models.CharField(max_length=200)
    years_exp = models.IntegerField(default=0)
    years_played = models.ManyToManyField(Year)
    #stats by year with team played for, gp, gs, min, fg%, ft%, reb, ast, blk, stl, pts
    mvp_years = models.ManyToManyField(Year)
    finals_mvp_years = models.ManyToManyField(Year)
    all_nba_years = models.ManyToManyField(Year)
    all_def_years = models.ManyToManyField(Year)
    twitter = models.URLField(unique=True)
    photo = models.URLField(unique=True)

    def __unicode__(self):
        return self.name

class Year(models.Model) :
    year = models.CharField(max_length=4, unique=True)
    all_nba = models.ManyToManyField(Player)
    all_def = models.ManyToManyField(Player)
    finals_mvp = models.ForeignKey(Player)
    champion = models.ForeignKey(Team)
    finals_logo = models.URLField(unique=True)
    finals_recap = models.TextField()

    def __unicode__(self):
        return self.year

