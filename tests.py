from django.test import TestCase
from django.db.utils import IntegrityError
from nba.testapp1.models import Player, Team, Year
import requests


class ModelsTestCase(TestCase):

    # test /api/teams/ - class TeamList from API
    def test_API_TeamList1(self):
        response = requests.get("http://nbadb.pythonanywhere.com/api/teams/")
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 10)
    def test_API_TeamList2(self):
        response = requests.get("http://nbadb.pythonanywhere.com/api/teamss/")
        self.assertEqual(response.status_code, 404)
    def test_API_TeamList3(self):
        response = requests.get("http://nbadb.pythonanywhere.com/api/teams/")
        data = response.json()
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(data[9], {"id": 10, "name": "Thunder", "location": "Oklahoma City, OK", "coach": "Scott Brooks", "gm": "Sam Presti", "owner": "Professional Basketball Club LLC", "twitter": "https://twitter.com/okcthunder", "logo": "http://img2.wikia.nocookie.net/__cb20120119223616/nba2k/images/7/74/Oklahoma_City_Thunder_Logo.png"})
        self.assertEqual(data[9]["id"], 10)

    # test /api/teams/{id}/ - class TeamDetail from API
    def test_API_TeamDetail1(self):
        response = requests.get("http://nbadb.pythonanywhere.com/api/teams/1/")
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 16)
    def test_API_TeamDetail2(self):
        response = requests.get("http://nbadb.pythonanywhere.com/api/teams/0/")
        self.assertEqual(response.status_code, 404)
    def test_API_TeamDetail3(self):
        response = requests.get("http://nbadb.pythonanywhere.com/api/teams/1/")
        data = response.json()
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(data, {"id": 1, "name": "Spurs", "location": "San Antonio, TX", "coach": "Gregg Popovich", "gm": "R. C. Buford", "owner": "Peter Holt", "twitter": "https://twitter.com/spurs", "logo": "http://www.sports-logos-screensavers.com/user/San_Antonio_Spurs2.jpg"})
        self.assertEqual(data["name"], "Spurs")
        self.assertEqual(len(data), 16)

    # test /api/players/ - class PlayerList from API
    def test_API_PlayerList1(self):
        response = requests.get("http://nbadb.pythonanywhere.com/api/players/")
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 11)
    def test_API_PlayerList2(self):
        response = requests.get("http://nbadb.pythonanywhere.com/api/playerss/")
        self.assertEqual(response.status_code, 404)
    def test_API_PlayerList3(self):
        response = requests.get("http://nbadb.pythonanywhere.com/api/players/")
        data = response.json()
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(data[0], {"id": 1, "name": "Tim Duncan", "position": "PF", "education": "Wake Forest", "years_exp": 17, "twitter": "https://twitter.com/TimSlamDuncan", "twitter_widget": "492366152106926082", "nickname": "\"The Big Fundamental\"", "photo": "http://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/215.png&w=350&h=254", "highlights": "https://www.youtube.com/embed/3uTCIPiuG5A", "current_team": "Spurs"})
        self.assertEqual(data[0]["id"], 1)

    # test /api/players/{id}/ - class PlayerDetail from API
    def test_API_PlayerDetail1(self):
        response = requests.get("http://nbadb.pythonanywhere.com/api/players/1/")
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 27)
    def test_API_PlayerDetail2(self):
        response = requests.get("http://nbadb.pythonanywhere.com/api/players/12/")
        self.assertEqual(response.status_code, 404)
    def test_API_PlayerDetail3(self):
        response = requests.get("http://nbadb.pythonanywhere.com/api/players/5/")
        data = response.json()
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(data, {"id": 5, "name": "Dwyane Wade", "position": "SG", "education": "Marquette", "years_exp": 11, "twitter": "https://twitter.com/DwyaneWade", "twitter_widget": "492366409570062336", "nickname": "\"Flash\"", "photo": "http://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/1987.png&w=350&h=254", "highlights": "https://www.youtube.com/embed/pPVzvf3nPxQ", "current_team": "Heat"})
        self.assertEqual(data["name"], "Dwyane Wade")
        self.assertEqual(len(data), 27)

     # test /api/years/ - class YearList from API
    def test_API_YearList1(self):
        response = requests.get("http://nbadb.pythonanywhere.com/api/years/")
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 10)
    def test_API_YearList2(self):
        response = requests.get("http://nbadb.pythonanywhere.com/api/yearss/")
        self.assertEqual(response.status_code, 404)
    def test_API_YearList3(self):
        response = requests.get("http://nbadb.pythonanywhere.com/api/years/")
        data = response.json()
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(data[2], {"id": 3, "year": "2007", "finals_logo": "http://upload.wikimedia.org/wikipedia/en/7/79/2007_NBA_Finals.png", "finals_recap": "The 2007 NBA Finals was the championship series of the 2006\u201307 National Basketball Association season, and was the conclusion of the 2007 NBA Playoffs. The best-of-seven series was played between the Western Conference champion San Antonio Spurs and the Eastern Conference champion Cleveland Cavaliers. This was Cleveland's first trip to the NBA Finals in their franchise history and San Antonio's fourth. The Spurs swept the Cavaliers 4-0. Tony Parker was named the series' MVP. The series was televised on ABC under the ESPN on ABC branding, and produced low television ratings.\r\n", "highlights": "https://www.youtube.com/embed/9aF6RJCfqf4"})
        self.assertEqual(data[2]["year"], "2007")

    # test /api/years/{id}/ - class YearDetail from API
    def test_API_YearDetail1(self):
        response = requests.get("http://nbadb.pythonanywhere.com/api/years/1/")
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 10)
    def test_API_YearDetail2(self):
        response = requests.get("http://nbadb.pythonanywhere.com/api/years/0/")
        self.assertEqual(response.status_code, 404)
    def test_API_YearDetail3(self):
        response = requests.get("http://nbadb.pythonanywhere.com/api/years/10/")
        data = response.json()
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(data, {"id": 10, "year": "2014", "finals_logo": "http://sports-glutton.com/wp-content/uploads/2013/06/2013-NBA-Finals.jpg", "finals_recap": "The 2014 NBA Finals was the championship series of the 2013\u201314 season of the National Basketball Association (NBA) and the conclusion of the season's playoffs. The Western Conference champion San Antonio Spurs defeated the Eastern Conference champion Miami Heat in five games (4\u20131) for the Spurs' fifth NBA championship in the franchise's history. The Spurs outscored the Heat in the series by the largest average point differential (14.0) in Finals history. San Antonio's Kawhi Leonard was named the Finals Most Valuable Player (MVP), and became the third-youngest recipient of the award.", "highlights": "https://www.youtube.com/embed/xnIjCqO7W0g"})
        self.assertEqual(data["year"], "2014")
        self.assertEqual(len(data), 10)

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

    def test_search1(self):
        response = requests.get("http://nbadb.pythonanywhere.com/search/?q=rose")
        self.assertEqual(response.status_code,200)

    def test_search2(self):
        response = requests.get("http://nbadb.pythonanywhere.com/search/?q=sdfe")
        self.assertEqual(response.status_code,200)

    def test_search3(self):
        response = requests.get("http://nbadb.pythonanywhere.com/search/?q=bryant+duncan+rose")
        self.assertEqual(response.status_code,200)

