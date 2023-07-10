from rest_framework import generics
from django.shortcuts import render
from process import serializers
from process.models import ForestLetter, ForestUser, Region, UserLevel

from process.serializers import ForestletterSerializer, RegionSerializer, UserLevelSerializer, UserSerializer, genNumSerializer

# Create your views here.
class RegionDetail(generics.ListCreateAPIView):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()
    # pagination_class = LimitOffsetPagination

class RegionList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()

""" Userlevel view  """
class UserLevelDetail(generics.ListCreateAPIView):
    serializer_class = UserLevelSerializer
    queryset = UserLevel.objects.all()
    # pagination_class = LimitOffsetPagination
    
class UserLevelList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserLevelSerializer
    queryset = UserLevel.objects.all()

class UserDetail(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    # pagination_class = LimitOffsetPagination
    def get_queryset(self):
        querySet = ForestUser.objects.all()
        region_id = self.request.query_params.get('region')
        level_id  = self.request.query_params.get('level')
    

        if region_id is not None  and level_id is None:
            querySet = querySet.filter(region_id = region_id)
            if not querySet:
                raise serializers.ValidationError({"authorize": "No Records Found."})

        elif region_id is None and  level_id is not None:
            querySet = querySet.filter(region_id = region_id,level_id=level_id)
            if not querySet:
                raise serializers.ValidationError({"authorize": "No Records Found."})
                
        elif region_id is not None and level_id is not None:
            querySet = querySet.filter(region_id = region_id, level_id=level_id)
            if not querySet:
                raise serializers.ValidationError({"authorize": "No Records Found."})
                
        return querySet

class UserList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = ForestUser.objects.all()
    
class ForestLetterDetail(generics.ListCreateAPIView):
    serializer_class = ForestletterSerializer
    queryset = ForestLetter.objects.all()
    
class ForestLetterList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ForestletterSerializer
    queryset = ForestLetter.objects.all()
    
class RetrieveGenNum(generics.RetrieveAPIView):
    serializer_class = genNumSerializer