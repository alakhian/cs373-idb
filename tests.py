from django.test import TestCase
from django.db.utils import IntegrityError
from nba.testapp1.models import Player, Team, Year

class ModelsTestCase(TestCase):

    # test creation (3 object tests)
    def test_Team1(self):
        lal = Team.objects.create(name="Lakers", location="Los Angelos", coach="vacant", gm="Mitch Kupchak", owner= "Jerry Buss", twitter="http://twitter.com/lakers", twitter_widget="9999", logo="http://imgur.com/lakers", finals_years="2005, 2006", mvps="Kobe Bryant", finals_mvps="Kobe Bryant")
        self.assertEqual(lal.name, "Lakers")
        self.assertEqual(lal.location, "Los Angelos")
        self.assertEqual(lal.coach, "vacant")
        self.assertEqual(lal.gm, "Mitch Kupchak")
        self.assertEqual(lal.owner, "Jerry Buss")
        self.assertEqual(lal.twitter, "http://twitter.com/lakers")
        self.assertEqual(lal.logo, "http://imgur.com/lakers")
        self.assertEqual(lal.twitter_widget, "9999")
        self.assertEqual(lal.finals_years, "2005, 2006")
        self.assertEqual(lal.mvps, "Kobe Bryant")
        self.assertEqual(lal.finals_mvps, "Kobe Bryant")

    def test_Player1(self):
        lal = Team.objects.create(name="Lakers", location="Los Angelos", coach="vacant", gm="Mitch Kupchak", owner= "Jerry Buss", twitter="http://twitter.com/lakers", twitter_widget="9999", logo="http://imgur.com/lakers", finals_years="2005, 2006", mvps="Kobe Bryant", finals_mvps="Kobe Bryant")
        kobe = Player.objects.create(name="Kobe Bryant", position="SG", education="HS", years_exp=15, twitter="http://twitter.com/kobebryant", twitter_widget="5000", nickname="Black Mamba", photo="http://imgur.com/kobe", highlights="http://youtube.com", current_team=lal, gp=1100, gs=1080, minpg=33.0, fgperc=0.450, ftperc=0.750, reb=4.5, ast=5.0, blk=0.5, stl=1.0, pts=27.5, finals_years="2003, 2005, 2006", finals_teams="Lakers", mvp_years="2006", finalsmvp_years="2006, 2008", allnba_years="2003, 2004", alldef_years="2000, 2002")
        self.assertEqual(kobe.name, "Kobe Bryant")
        self.assertEqual(kobe.position, "SG")
        self.assertEqual(kobe.education, "HS")
        self.assertEqual(kobe.years_exp, 15)
        self.assertEqual(kobe.twitter, "http://twitter.com/kobebryant")
        self.assertEqual(kobe.twitter_widget, "5000")
        self.assertEqual(kobe.nickname, "Black Mamba")
        self.assertEqual(kobe.photo, "http://imgur.com/kobe")
        self.assertEqual(kobe.highlights, "http://youtube.com")
        self.assertEqual(kobe.current_team, lal)
        self.assertEqual(kobe.gp, 1100)
        self.assertEqual(kobe.gs, 1080)
        self.assertEqual(kobe.minpg, 33.0)
        self.assertEqual(kobe.fgperc, 0.450)
        self.assertEqual(kobe.ftperc, 0.750)
        self.assertEqual(kobe.reb, 4.5)
        self.assertEqual(kobe.ast, 5.0)
        self.assertEqual(kobe.blk, 0.5)
        self.assertEqual(kobe.stl, 1.0)
        self.assertEqual(kobe.pts, 27.5)
        self.assertEqual(kobe.finals_years, "2003, 2005, 2006")
        self.assertEqual(kobe.finals_teams, "Lakers")
        self.assertEqual(kobe.mvp_years, "2006")
        self.assertEqual(kobe.finalsmvp_years, "2006, 2008")
        self.assertEqual(kobe.allnba_years, "2003, 2004")
        self.assertEqual(kobe.alldef_years, "2000, 2002")


    def test_Year1(self):
        lal = Team.objects.create(name="Lakers", location="Los Angelos", coach="vacant", gm="Mitch Kupchak", owner= "Jerry Buss", twitter="http://twitter.com/lakers", twitter_widget="9999", logo="http://imgur.com/lakers", finals_years="2005, 2006", mvps="Kobe Bryant", finals_mvps="Kobe Bryant")
        kobe = Player.objects.create(name="Kobe Bryant", position="SG", education="HS", years_exp=15, twitter="http://twitter.com/kobebryant", twitter_widget="5000", nickname="Black Mamba", photo="http://imgur.com/kobe", highlights="http://youtube.com", current_team=lal, gp=1100, gs=1080, minpg=33.0, fgperc=0.450, ftperc=0.750, reb=4.5, ast=5.0, blk=0.5, stl=1.0, pts=27.5, finals_years="2003, 2005, 2006", finals_teams="Lakers", mvp_years="2006", finalsmvp_years="2006, 2008", allnba_years="2003, 2004", alldef_years="2000, 2002")
        y2006 = Year.objects.create(year="2006", finals_logo="http://imgur.com/2006", finals_recap="Kobe wins", highlights="http://youtube.com/2006", all_nba="Kobe, Nash", all_def="Kevin Garnett", reg_mvp=kobe, finals_mvp=kobe, champion=lal)
        self.assertEqual(y2006.year, "2006")
        self.assertEqual(y2006.finals_logo, "http://imgur.com/2006")
        self.assertEqual(y2006.finals_recap, "Kobe wins")
        self.assertEqual(y2006.highlights, "http://youtube.com/2006")
        self.assertEqual(y2006.all_nba, "Kobe, Nash")
        self.assertEqual(y2006.all_def, "Kevin Garnett")
        self.assertEqual(y2006.reg_mvp, kobe)
        self.assertEqual(y2006.champion, lal)


    #test defaults of objects (3)
    def test_Team2(self):
        sa = Team.objects.create(name="Spurs", location="San Antonio", coach="Pop", gm="rich guy 1", owner="rich guy 2", twitter="http://twitter.com/spurs", logo="http://imgur.com/spurs")
        self.assertEqual(sa.name, "Spurs")
        self.assertEqual(sa.location, "San Antonio")
        self.assertEqual(sa.coach, "Pop")
        self.assertEqual(sa.gm, "rich guy 1")
        self.assertEqual(sa.owner, "rich guy 2")
        self.assertEqual(sa.twitter, "http://twitter.com/spurs")
        self.assertEqual(sa.twitter_widget, "")
        self.assertEqual(sa.logo, "http://imgur.com/spurs")
        self.assertEqual(sa.finals_years, "")
        self.assertEqual(sa.mvps, "")
        self.assertEqual(sa.finals_mvps, "")

    def test_Player2(self):
        tim = Player.objects.create(name="Tim Duncan", position="PF", education="Wake Forest", twitter="http://twitter.com/timduncan", photo="http://imgur.com/tim")
        self.assertEqual(tim.name, "Tim Duncan")
        self.assertEqual(tim.position, "PF")
        self.assertEqual(tim.education, "Wake Forest")
        self.assertEqual(tim.years_exp, 0)
        self.assertEqual(tim.twitter, "http://twitter.com/timduncan")
        self.assertEqual(tim.twitter_widget, "")
        self.assertEqual(tim.nickname, "")
        self.assertEqual(tim.photo, "http://imgur.com/tim")
        self.assertEqual(tim.highlights, "")
        self.assertEqual(tim.gp, 0)
        self.assertEqual(tim.gs, 0)
        self.assertEqual(tim.minpg, 0)
        self.assertEqual(tim.fgperc, 0)
        self.assertEqual(tim.ftperc, 0)
        self.assertEqual(tim.reb, 0)
        self.assertEqual(tim.ast, 0)
        self.assertEqual(tim.blk, 0)
        self.assertEqual(tim.stl, 0)
        self.assertEqual(tim.pts, 0)
        self.assertEqual(tim.finals_years, "")
        self.assertEqual(tim.finals_teams, "")
        self.assertEqual(tim.mvp_years, "")
        self.assertEqual(tim.finalsmvp_years, "")
        self.assertEqual(tim.allnba_years, "")
        self.assertEqual(tim.alldef_years, "")

    def test_Year2(self):
        y2007 = Year.objects.create(year="2007", finals_logo="http://imgur.com/2007", finals_recap= "")
        self.assertEqual(y2007.year, "2007")
        self.assertEqual(y2007.finals_logo, "http://imgur.com/2007")
        self.assertEqual(y2007.finals_recap, "")
        self.assertEqual(y2007.highlights, "")
        self.assertEqual(y2007.all_nba, "")
        self.assertEqual(y2007.all_def, "")

    # test trying to create objects with conflicting unique fields
    def test_Player3(self):
        lal = Team.objects.create(name="Lakers", location="Los Angelos", coach="vacant", gm="Mitch Kupchak", owner= "Jerry Buss", twitter="http://twitter.com/lakers", twitter_widget="9999", logo="http://imgur.com/lakers", finals_years="2005, 2006", mvps="Kobe Bryant", finals_mvps="Kobe Bryant")
        kobe = Player.objects.create(name="Kobe Bryant", position="SG", education="HS", years_exp=15, twitter="http://twitter.com/kobebryant", twitter_widget="5000", nickname="Black Mamba", photo="http://imgur.com/kobe", highlights="http://youtube.com", current_team=lal, gp=1100, gs=1080, minpg=33.0, fgperc=0.450, ftperc=0.750, reb=4.5, ast=5.0, blk=0.5, stl=1.0, pts=27.5, finals_years="2003, 2005, 2006", finals_teams="Lakers", mvp_years="2006", finalsmvp_years="2006, 2008", allnba_years="2003, 2004", alldef_years="2000, 2002")
        try :
            kobe2 = Player.objects.create(name="Kobe Bryant", position="SG", education="HS", years_exp=15, twitter="http://twitter.com/kobebryant", twitter_widget="5000", nickname="Black Mamba", photo="http://imgur.com/kobe", highlights="http://youtube.com", current_team=lal, gp=1100, gs=1080, minpg=33.0, fgperc=0.450, ftperc=0.750, reb=4.5, ast=5.0, blk=0.5, stl=1.0, pts=27.5, finals_years="2003, 2005, 2006", finals_teams="Lakers", mvp_years="2006", finalsmvp_years="2006, 2008", allnba_years="2003, 2004", alldef_years="2000, 2002")
            self.assertFalse(kobe2.name == kobe.name)
        except IntegrityError :
            assert True

    def test_Team3(self):
        sa = Team.objects.create(name="Spurs", location="San Antonio", coach="Pop", gm="rich guy 1", owner="rich guy 2", twitter="http://twitter.com/spurs", logo="http://imgur.com/spurs")
        try :
            sa2 = Team.objects.create(name="Spurs", location="San Antonio", coach="Pop", gm="rich guy 1", owner="rich guy 2", twitter="http://twitter.com/spurs", logo="http://imgur.com/spurs")
            self.assertFalse(sa.name == sa2.name)
        except IntegrityError :
            assert True

    def test_Year3(self):
        y2007 = Year.objects.create(year="2007", finals_logo="http://imgur.com/2007", finals_recap= "")
        try :
            y07 = Year.objects.create(year="2007", finals_logo="http://imgur.com/2007", finals_recap= "")
            self.assertFalse(y2007.year == y07.year and y2007.finals_logo == y07.finals_logo)
        except IntegrityError :
            assert True