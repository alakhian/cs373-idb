from .models import Team, Player, Year

from rest_framework import serializers

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            'id',
            'name',
            'location',
            'coach',
            'gm',
            'owner',
            'twitter',
            'twitter_widget',
            'logo',
            'finals_years',
            'mvps',
            'finals_mvps',
            'stadium',
            'map_lat',
            'map_lng',
            'map_address'
        )


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = (
            'id',
            'name',
            'position',
            'education',
            'years_exp',
            'twitter',
            'twitter_widget',
            'nickname',
            'photo',
            'highlights',
            'current_team',
            'gp',
            'gs',
            'minpg',
            'fgperc',
            'ftperc',
            'reb',
            'ast',
            'blk',
            'stl',
            'pts',
            'finals_years',
            'finals_teams',
            'mvp_years',
            'finalsmvp_years',
            'allnba_years',
            'alldef_years'
        )

class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = (
            'id',
            'year',
            'finals_logo',
            'finals_recap',
            'highlights',
            'all_nba',
            'all_def',
            'reg_mvp',
            'finals_mvp',
            'champion'
        )
