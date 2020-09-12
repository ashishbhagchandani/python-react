from rest_framework import serializers
from api.models import movie

#lead serializers
class movieSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie
        fields = '__all__'