from django.db import models


# Models for the NBA app

class Team(models.Model) :
    """
    Contains information for a Team that is current and will not change
    Each Team has multiple TeamYear's (One-To-Many)
    """
    name = models.CharField(max_length=20, unique=True)
    location = models.CharField(max_length=30, unique=True)
    coach = models.CharField(max_length=30, unique=True)
    gm = models.CharField(max_length=30, unique=True)
    owner = models.CharField(max_length=30)
    twitter = models.URLField(unique=True)
    logo = models.URLField(unique=True)
    finals_years = models.CharField(max_length=200)
    mvps = models.CharField(max_length=200)
    finals_mvps = models.CharField(max_length=200)


    def __str__(self) :
        return "name: " + self.name + "\n" \
               "location: " + self.location + "\n" \
               "coach: " + self.coach + "\n" \
               "gm: " + self.gm + "\n" \
               "owner: " + self.owner + "\n" \
               "twitter: " + str(self.twitter) + "\n" \
               "logo: " + str(self.logo) + "\n"

    class Meta:
        app_label = 'nba'

class Player(models.Model) :
    """
    Contains information about a Player that is current and will not change
    Each Player has multiple PlayerYear's (One-To-Many)
    """
    name = models.CharField(max_length=30, unique=True)
    position = models.CharField(max_length=2)
    education = models.CharField(max_length=20)
    years_exp = models.IntegerField(default=0)
    twitter = models.URLField(unique=True)
    photo = models.URLField(unique=True)
    #stats are career averages
    gp = models.IntegerField(default=0)
    gs = models.IntegerField(default=0)
    minpg = models.FloatField()
    fgperc = models.FloatField()
    ftperc = models.FloatField()
    reb = models.FloatField()
    ast = models.FloatField()
    blk = models.FloatField()
    stl = models.FloatField()
    pts = models.FloatField()
    finals_years = models.CharField(max_length=200)
    finals_teams = models.CharField(max_length=500)
    mvp_years = models.CharField(max_length=200)
    finalsmvp_years = models.CharField(max_length=200)
    allnba_years = models.CharField(max_length=200)
    alldef_years = models.CharField(max_length=200)


    def __str__(self) :
        return "name: " + self.name + "\n" \
               "position: " + self.position + "\n" \
               "education: " + self.education + "\n" \
               "years of experience: " + self.years_exp + "\n" \
               "twitter: " + str(self.twitter) + "\n" \
               "photo: " + str(self.photo) + "\n"

    class Meta:
        app_label = 'nba'

class Year(models.Model) :
    """
    Contains information about a certain Year
    Each Year has multiple PlayerYear's and TeamYear's (One-To-Many)
    """
    year = models.CharField(max_length=4, unique=True)
    all_nba = models.ManyToManyField(Player)
    all_def = models.ManyToManyField(Player)
    finals_mvp = models.ForeignKey(Player)
    champion = models.ForeignKey(Team)
    finals_logo = models.URLField(unique=True)
    finals_recap = models.TextField()


    class Meta:
        app_label = 'nba'

"""
class PlayerYear(models.Model) :
    
    #Contains information/statistics about a Player during a certain Year
    
    year = models.ForeignKey(Year)
    player = models.ForeignKey(Player)
    team = models.ForeignKey(Team)
    
    mvp = models.BooleanField()
    finals_mvp = models.BooleanField()
    all_nba = models.BooleanField()
    all_def = models.BooleanField()


    class Meta:
        app_label = 'nba'
"""

"""
class TeamYear(models.Model) :
    
    #Contains information/statistics about a Team during a certain Year
    
    team = models.ForeignKey(Team)
    year = models.ForeignKey(Year)
    wins = models.IntegerField()
    losses = models.IntegerField()
    playoffrecap = models.TextField()


    class Meta:
        app_label = 'nba'

"""

