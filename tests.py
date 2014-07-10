from django.utils import unittest
from nba.models import Player, Team, Year, PlayerYear, TeamYear

class ModelsTestCase(unittest.TestCase):

    #-----
    # test Player
    #-----

    #test creation
    def test_Player1(self):
        player_1 = Player.objects.create(name="Bob Joe", position="PG", education="University of Texas", years_exp=0, twitter= "https://", photo= "https://")
        self.assertEqual(player_1.name, "Bob Joe")
        self.assertEqual(player_1.position, "PG")
        self.assertEqual(player_1.education, "University of Texas")
        self.assertEqual(player_1.years_exp, 0)
        self.assertEqual(player_1.twitter, "https://")
        self.assertEqual(player_1.photo, "https://")

    #test defaulting years_exp to 0
    def test_Player2(self):
        p = Player.objects.create(name="Kobe", position="SG", education="Fake High School", twitter="http://", photo= "http://")
        self.assertEqual(p.years_exp, 0)
    
    #test str
    def test_Player3(self):
        p = Player.objects.create(name="Kobe Bryant", position="SG", education="Fake High School", twitter="http://twitter.com", photo= "https://imgur.com")
        self.assertEqual(str(p), "name: Kobe Bryant\nposition: SG\neducation: Fake High School\nyears of experience: 0\n")


    #-----
    # Test Team
    #-----
    
    #test creation
    def test_Team1(self):
        lal = Team.objects.create(name="Lakers", location="Los Angelos", coach="Phil Jackson", gm="some rich guy", owner= "some rich guy2", twitter="http://twitter.com/lakers", logo="http://imgur.com/lakers")
        self.assertEqual(lal.name, "Lakers")
        self.assertEqual(lal.location, "Los Angelos")
        self.assertEqual(lal.coach, "Phil Jackson")
        self.assertEqual(lal.gm, "some rich guy")
        self.assertEqual(lal.owner, "some rich guy2")
        self.assertEqual(lal.twitter, "http://twitter.com/lakers")
        self.assertEqual(lal.logo, "http://imgur.com/lakers")

    #test str
    def test_Team2(self):
        s = Team.objects.create(name="Spurs", location="San Antonio", coach="Pop", gm="genious", owner="genious2", twitter="http://twitter.com/spurs", logo="http://imgur.com/spurs")
        self.assertEqual(str(s), "name: Spurs\nlocation: San Antonio\ncoach: Pop\ngm: genious\nowner: genious2\n")


    #-----
    # test Year
    #-----

    # test create along with use of foreign keys for player/team
    def test_Year1(self):
        p = Player.objects.create(name="Kobe2", position="SG", education="Fake High School", twitter="http://2", photo= "http://2")
        lal2 = Team.objects.create(name="Lakers2", location="Los Angelos", coach="Phil Jackson2", gm="some rich guy2", owner= "some rich guy23", twitter="http://twitter.com/lakers2", logo="http://imgur.com/lakers2")
        y2005 = Year.objects.create(year="2005", all_nba="some rejects", all_def="some more rejects", finals_mvp = p, champion= lal2, finals_logo="https://2005finals", finals_recap="somebody won")
        self.assertEqual(y2005.year, "2005")
        self.assertEqual(y2005.all_nba, "some rejects")
        self.assertEqual(y2005.all_def, "some more rejects")
        self.assertEqual(y2005.finals_mvp.name, "Kobe2")
        self.assertEqual(y2005.champion.name, "Lakers2")
        self.assertEqual(y2005.finals_logo, "https://2005finals")
        self.assertEqual(y2005.finals_recap, "somebody won")


    #-----
    # test PlayerYear
    #-----
    
    #test create with Player, team, Year foreign keys
    def test_PlayerYear1(self):
        p = Player.objects.create(name="Kobe3", position="SG", education="Fake High School", twitter="http://3", photo= "http://3")
        lal3 = Team.objects.create(name="Lakers3", location="Los Angelos", coach="Phil Jackson3", gm="rich1", owner= "rich2", twitter="http://twitter.com/lakers3", logo="http://imgur.com/lakers3")
        y2006 = Year.objects.create(year="2006", all_nba="some rejects", all_def="some more rejects", finals_mvp = p, champion= lal3, finals_logo="https://2006finals", finals_recap="somebody won")
        kobe06 = PlayerYear.objects.create(year=y2006, player=p, team=lal3, minpg=0.0, fgperc=.000, ftperc=.000, reb=0.0, ast=0.0, blk=0.0, stl=0.0, pts=0.0, mvp=False, finals_mvp=True, all_nba=True, all_def=False)
        self.assertEqual(kobe06.year.year, "2006")
        self.assertEqual(kobe06.player.name, "Kobe3")
        self.assertEqual(kobe06.team.name, "Lakers3")
        self.assertEqual(kobe06.gp, 0)
        self.assertEqual(kobe06.gs, 0)
        self.assertEqual(kobe06.minpg, 0.0)
        self.assertEqual(kobe06.fgperc, .000)
        self.assertEqual(kobe06.ftperc, .000)
        self.assertEqual(kobe06.reb, 0.0)
        self.assertEqual(kobe06.ast, 0.0)
        self.assertEqual(kobe06.blk, 0.0)
        self.assertEqual(kobe06.stl, 0.0)
        self.assertEqual(kobe06.mvp, False)
        self.assertEqual(kobe06.finals_mvp, True)
        self.assertEqual(kobe06.all_nba, True)
        self.assertEqual(kobe06.all_def, False)

        

    #-----
    # test TeamYear
    #-----

    #test create with team and year
    def test_TeamYear1(self):
        p = Player.objects.create(name="Kobe4", position="SG", education="Fake High School", twitter="http://4", photo= "http://4")
        lal4 = Team.objects.create(name="Lakers4", location="Los Angelos", coach="Phil Jackson4", gm="rich3", owner= "rich4", twitter="http://twitter.com/lakers4", logo="http://imgur.com/lakers4")
        y2007 = Year.objects.create(year="2007", all_nba="some rejects", all_def="some more rejects", finals_mvp = p, champion= lal4, finals_logo="https://2007finals", finals_recap="somebody won")
        lakers07 = TeamYear.objects.create(team=lal4, year=y2007, wins=82, losses=0, playoffrecap="demolished everyone, won championship")
        self.assertEqual(lakers07.team.name, "Lakers4")
        self.assertEqual(lakers07.year.year, "2007")
        self.assertEqual(lakers07.wins, 82)
        self.assertEqual(lakers07.losses, 0)
        self.assertEqual(lakers07.playoffrecap, "demolished everyone, won championship")






