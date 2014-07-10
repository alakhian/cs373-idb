from django.contrib import admin
from nba.testapp1.models import Team, Player, Year

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Year)