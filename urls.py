from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from django.views.generic import ListView, DetailView
from nba.testapp1.models import Team, Player, Year
#from django.views.generic import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
        # This is going to be our home view.
        # We'll uncomment it later
    url(r'^$', 'nba.testapp1.views.home', name='home'),
    #players, teams, and years view
    url(r'^players/$', 'nba.testapp1.views.PlayersAll'),
    url(r'^teams/$', 'nba.testapp1.views.TeamsAll'),
    url(r'^years/$', 'nba.testapp1.views.YearsAll'),

    url(r'^players/(?P<pk>\d+)/$', DetailView.as_view(
                        model = Player,
                        template_name="player.html")),
    url(r'^teams/(?P<pk>\d+)/$', DetailView.as_view(
                        model = Team,
                        template_name="team.html")),
    url(r'^years/(?P<pk>\d+)/$', DetailView.as_view(
                        model = Year,
                        template_name="year.html")),
        # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

        # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^testapp1/', include('nba.testapp1.urls')),


)