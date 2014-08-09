from django.db import models

# Models for the NBA app

class Team(models.Model) :
    """
    Contains the information for an NBA Organization
    """
    name = models.CharField(max_length=20, unique=True)
    location = models.CharField(max_length=30, unique=True)
    coach = models.CharField(max_length=30, unique=True)
    gm = models.CharField(max_length=30, unique=True)
    owner = models.CharField(max_length=50)
    twitter = models.URLField(unique=True)
    twitter_widget = models.CharField(max_length=500, default="")
    logo = models.URLField(unique=True)
    finals_years = models.CharField(max_length=200, default="")
    mvps = models.CharField(max_length=200, default="")
    finals_mvps = models.CharField(max_length=200, default="")
    stadium = models.CharField(max_length=200, default="")
    map_lat = models.CharField(max_length=200, default="")
    map_lng = models.CharField(max_length=200, default="")
    map_address = models.CharField(max_length=200, default="")



    #years with results of season (record, playoff recap, mvp awards)

    def __unicode__(self) :
        return self.name
    """
    def __str__(self) :
        return "name: " + self.name + "\n" \
               "location: " + self.location + "\n" \
               "coach: " + self.coach + "\n" \
               "gm: " + self.gm + "\n" \
               "owner: " + self.owner + "\n" \
               "twitter: " + str(self.twitter) + "\n" \
               "logo: " + str(self.logo) + "\n"
    """
    def get_absolute_url(self):
        return "/teams/%i/" % self.id

    #class Meta:
    #    app_label = 'nba'



class Player(models.Model) :
    """
    Contains information and statistics for a specific NBA player
    Also contains a link to one Team
    Multiple players can have a link to a single team
    """
    name = models.CharField(max_length=30, unique=True)
    position = models.CharField(max_length=2)
    education = models.CharField(max_length=40)
    years_exp = models.IntegerField(default=0)
    #stats by year with team played for, gp, gs, min, fg%, ft%, reb, ast, blk, stl, pts
    #awards for MVP, Finals MVP, all-NBA 1st team, all-defensive 1st team
    twitter = models.URLField(unique=True)
    twitter_widget = models.CharField(max_length=500, default="")
    nickname = models.CharField(max_length=40, default="")
    photo = models.URLField(unique=True)
    highlights = models.URLField(unique=True, default="")
    current_team = models.ForeignKey('Team', related_name='current_team', to_field='name', default='none')


    #stats are career averages
    gp = models.IntegerField(default=0)
    gs = models.IntegerField(default=0)
    minpg = models.FloatField(default=0)
    fgperc = models.FloatField(default=0)
    ftperc = models.FloatField(default=0)
    reb = models.FloatField(default=0)
    ast = models.FloatField(default=0)
    blk = models.FloatField(default=0)
    stl = models.FloatField(default=0)
    pts = models.FloatField(default=0)
    finals_years = models.CharField(max_length=200, default="")
    finals_teams = models.CharField(max_length=500, default="")
    mvp_years = models.CharField(max_length=200, default="")
    finalsmvp_years = models.CharField(max_length=200, default="")
    allnba_years = models.CharField(max_length=200, default="")
    alldef_years = models.CharField(max_length=200, default="")

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/players/%i/" % self.id
    """
    def __str__(self) :
        return "name: " + self.name + "\n" \
               "position: " + self.position + "\n" \
               "education: " + self.education + "\n" \
               "years of experience: " + self.years_exp + "\n" \
               "twitter: " + str(self.twitter) + "\n" \
               "photo: " + str(self.photo) + "\n"
    """
class Year(models.Model) :
    """
    Contains information about a NBA Season
    contains one link to an NBA Team and 2 links to NBA Players
    """
    year = models.CharField(max_length=4, unique=True)
    #all nba 1st team (players?)
    #all nba defensive (players?)
    #finals_mvp = models.ForeignKey(Player) (correct?)
    #champion = models.ForeignKey(Team) (correct?)
    finals_logo = models.URLField(unique=True)
    finals_recap = models.TextField()
    highlights = models.URLField(unique=True, default="")

    all_nba = models.CharField(max_length=500, default="")
    all_def = models.CharField(max_length=500, default="")
    reg_mvp = models.ForeignKey('Player', related_name='reg_mvp', to_field='name', default='none')
    finals_mvp = models.ForeignKey('Player', related_name='finals_mvp', to_field='name', default='none')
    champion = models.ForeignKey('Team', related_name='champion', to_field='name', default='none')


    def __unicode__(self):
        return self.year

    def get_absolute_url(self):
        return "/years/%i/" % self.id