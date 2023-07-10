from django.contrib.auth.models import User
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from process.models import ForestLetter, ForestUser, Region, UserLevel

class userSuperSerializer(serializers.ModelSerializer):
    class Meta:
        mode = User
        fields = ('__all__')
        
class genNumSerializer(serializers.ModelSerializer):
    class Meta:
        mode = ForestLetter
        fields = ('id')

class RegionSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Region
        fields = ('__all__')
        
class UserLevelSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = UserLevel
        fields = ('__all__')
        
class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ForestUser
        fields = ('__all__')
        depth = 1                         
        expandable_fields = {'region': (RegionSerializer, {'source': 'region_id', 'fields': ['region_id', 'region_txt']}),
                             'userlevel': (UserLevelSerializer, {'source': 'level_id', 'fields': ['level_id', 'level_name']}),
                            }

class ForestletterSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ForestLetter
        fields = ('__all__')                        
        expandable_fields = {'userlevel': (UserLevelSerializer, {'source': 'level_id', 'fields': ['level_id', 'level_name']}),}