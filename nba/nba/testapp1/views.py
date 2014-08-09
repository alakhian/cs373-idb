from django.shortcuts import render, render_to_response, RequestContext
#from django.template import RequestContext
from nba.testapp1.models import Player, Team, Year




from django.utils.safestring import SafeString
import re
from django.db.models import Q

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

def About(request):
    return render_to_response('about.html', locals(), context_instance=RequestContext(request))

def API(request):
    return render_to_response('API.html', locals(), context_instance=RequestContext(request))

def API1(request):
    url = "https://notoriousbiginteger.pythonanywhere.com/cuisines/json"
    json_obj = urllib2.urlopen(url)
    data = json.load(json_obj)
    return render(request, 'API.html', {'data': SafeString(data)})

def home(request):
    return render_to_response('index.html', locals(),
                                context_instance=RequestContext(request))


def normalize_query(query_string, findterms=re.compile(r'"([^"]+)"|(\S+)').findall, normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    query = None # Query to search for every search term
    and_query = None
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
            and_query = or_query
        else:
            query = query | or_query
            and_query = and_query & or_query
    return query, and_query

def search(request):
    query_string = ''
    query_list = ''
    team_results = None
    team_results_and = None
    player_results = None
    player_results_and = None
    year_results = None
    year_results_and = None
    team_fields = ['name', 'location', 'coach', 'gm', 'owner', 'finals_years', 'finals_mvps', 'stadium', 'map_lat', 'map_lng', 'map_lng', 'map_address']
    player_fields = ['name', 'position', 'education', 'years_exp', 'twitter_widget', 'nickname', 'finals_years', 'finals_teams', 'mvp_years', 'finalsmvp_years', 'allnba_years', 'alldef_years']
    year_fields = ['year', 'finals_recap', 'all_nba', 'all_def']
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET.get('q')
        query_list = normalize_query(query_string)
        query_list.sort()

        entry_query, and_entry_query = get_query(query_string, team_fields)
        team_results = Team.objects.filter(entry_query)
        team_results_and = Team.objects.filter(and_entry_query)

        entry_query, and_entry_query = get_query(query_string, player_fields)
        player_results = Player.objects.filter(entry_query)
        player_results_and = Player.objects.filter(and_entry_query)

        entry_query, and_entry_query = get_query(query_string, year_fields)
        year_results = Year.objects.filter(entry_query)
        year_results_and = Year.objects.filter(and_entry_query)
        #if ('format' in request.GET) and request.GET['format'].strip() and request.GET.get('format') == "json":
        #    data = { 'query_string': query_string, 'query_list' : query_list, 'Or_Colleges' : list(team_results.values()), 'And_Colleges' : list(team_results_and.values()), 'Or_Majors': list(player_results.values()), 'And_Majors' : list(player_results_and.values()), 'Or_Courses' : list(year_results.values()), 'And_Courses' : list(year_results_and.values()) }
        #    return HttpResponse(json.dumps(data), 'application/json')
    return render_to_response('search/search.html', { 'query_string': query_string, 'query_list' : query_list, 'team' : list(team_results.values()), 'team_and' : list(team_results_and.values()), 'player': list(player_results.values()), 'player_and' : list(player_results_and.values()), 'year' : list(year_results.values()), 'year_and' : list(year_results_and.values()) }, context_instance=RequestContext(request))


"""


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:

        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.

    '''
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query


def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        entry_query = get_query(query_string, ['name', 'location',])

        found_entries = Team.objects.filter(entry_query).order_by('-pub_date')

    return render_to_response('search/search.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))
"""
