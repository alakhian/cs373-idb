from .models import Team, Player, Year
from .serializers import TeamSerializer, PlayerSerializer, YearSerializer

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response


class TeamList(APIView):
    def get (self, request, format=None):
        teams = Team.objects.all()
        serialized_teams = TeamSerializer(teams)
        return Response(serialized_teams.data)

class TeamDetail(APIView):
    def get_object(self, pk):
        try:
            return Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        team = self.get_object(pk)
        serialized_team = TeamSerializer(team)
        return Response(serialized_team.data)


class PlayerList(APIView):
    def get (self, request, format=None):
        players = Player.objects.all()
        serialized_players = PlayerSerializer(players)
        return Response(serialized_players.data)

class PlayerDetail(APIView):
    def get_object(self, pk):
        try:
            return Player.objects.get(pk=pk)
        except Player.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        player = self.get_object(pk)
        serialized_player = PlayerSerializer(player)
        return Response(serialized_player.data)


class YearList(APIView):
    def get (self, request, format=None):
        years = Year.objects.all()
        serialized_years = YearSerializer(years)
        return Response(serialized_years.data)

class YearDetail(APIView):
    def get_object(self, pk):
        try:
            return Year.objects.get(pk=pk)
        except Year.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        year = self.get_object(pk)
        serialized_year = YearSerializer(year)
        return Response(serialized_year.data)
