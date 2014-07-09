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

    def __unicode__(self) :
        return self.name

class Player(models.Model) :
    name = models.CharField(max_length=30, unique=True)
    position = models.CharField(max_length=2)
    education = models.CharField(max_length=200)
    years_exp = models.IntegerField(default=0)
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

class PlayerYear(models.Model) :
    year = models.ForeignKey(Year)
    player = models.ForeignKey(Player)
    team = models.ForeignKey(Team)
    gp = models.IntegerField(default=0)
    gs = models.IntegerField(default=0)
    minpg = models.FloatField()
    fgperc = models.FloatField()
    ftperc = models.FloatField()
    reb = models.IntegerField()
    ast = models.IntegerField()
    blk = models.IntegerField()
    stl = models.IntegerField()
    pts = models.FloatField()
    mvp = models.BooleanField()
    finals_mvp = models.BooleanField()
    all_nba = models.BooleanField()
    all_def = models.BooleanField()
    
    def __unicode__(self):
        return (self.player.name, self.year.year)

class TeamYear(models.Model) :
    year = models.ForeignKey(Year)
    wins = models.IntegerField()
    losses = models.IntegerField()
    playoffrecap = models.CharField() 

    

