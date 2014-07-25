from django.shortcuts import render, render_to_response, RequestContext
#from django.template import RequestContext
from nba.testapp1.models import Player, Team, Year
# Creating my views

def PlayersAll(request):
    players = Player.objects.all().order_by('name')
    context = {'players': players}
    return render_to_response('playersall.html', context, context_instance=RequestContext(request))

def TeamsAll(request):
    teams = Team.objects.all().order_by('name')
    context = {'teams': teams}
    return render_to_response('teamsall.html', context, context_instance=RequestContext(request))

def YearsAll(request):
    years = Year.objects.all().order_by('year')
    context = {'years': years}
    return render_to_response('yearsall.html', context, context_instance=RequestContext(request))

def home(request):
    return render_to_response('index.html', locals(),
                                context_instance=RequestContext(request))
