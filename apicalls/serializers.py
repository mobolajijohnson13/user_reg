from rest_framework import serializers 
from apicalls.models import Magazine
 
 
class MagazineSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Magazine
        fields = '__all__'