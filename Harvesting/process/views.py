from xml.sax import parseString
from django.http import HttpResponse

import pandas as pd
from rest_framework.views import APIView

import requests
from django.shortcuts import render
from process import serializers
from process.serializers import ChangePasswordSerializer, CoupWorkProgramSerializer,ForestletterSerializer, LetterTemplateSerializer, LetterToRMSerializer, MyTokenObtainPairSerializer, NumGenSerializer, RegionSerializer, RegisterSerializer, UpdateUserSerializer, UserLevelSerializer, UserSerializer, genNumSerializer, ScheduleItemsSerializer, ScheduleSerializer, PostViewSetSerializer
from process.models import CoupWorkProgram, ForestLetter, ForestUser, LetterTemplate, LetterToRM, Region, UserLevel, ScheduleItems, Schedule, Post
from django.contrib.auth.models import User
from django.shortcuts import redirect

from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken

from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

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

# User
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

# ForestLetter    
class ForestLetterDetail(generics.ListCreateAPIView):
    serializer_class = ForestletterSerializer
    queryset = ForestLetter.objects.all()
    
class ForestLetterList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ForestletterSerializer
    queryset = ForestLetter.objects.all()
    
# coupWorkProgram    
class coupWorkProgramDetail(generics.ListCreateAPIView):
    serializer_class = CoupWorkProgramSerializer
    queryset = CoupWorkProgram.objects.all()
    
class coupWorkProgramList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CoupWorkProgramSerializer
    queryset = CoupWorkProgram.objects.all()

# LetterToRM
class LetterToRMDetail(generics.ListCreateAPIView):
    serializer_class = LetterToRMSerializer
    queryset = LetterToRM.objects.all()
    
class LetterToRMList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LetterToRMSerializer
    queryset = LetterToRM.objects.all()
    
# LetterTemplate   
class LetterTemplateDetail(generics.ListCreateAPIView):
    serializer_class = LetterTemplateSerializer
    queryset = LetterTemplate.objects.all()
    
class LetterTemplateList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LetterTemplateSerializer
    queryset = LetterTemplate.objects.all()

# ScheduleItems    
class ScheduleItemsDetail(generics.ListCreateAPIView):
    serializer_class = ScheduleItemsSerializer
    queryset = ScheduleItems.objects.all()
    
class ScheduleItemsList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ScheduleItemsSerializer
    queryset = ScheduleItems.objects.all()
    
# Schedule    
class ScheduleDetail(generics.ListCreateAPIView):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()
    
class ScheduleList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()
    

 # RetrieveGenNum (this is working fine)
def get_last_inserted_row_number(request):
    serializer = NumGenSerializer()
    last_row_number = serializer.get_last_inserted_row_number()
    return HttpResponse(str(last_row_number))

class PostViewSet(APIView):
    permission_classes = []
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = FileSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

""" 

Extend user and authontication


 """
class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)

