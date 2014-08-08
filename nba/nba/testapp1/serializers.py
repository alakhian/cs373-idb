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
            'logo'
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
            'current_team'
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
        )
