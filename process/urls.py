from rest_framework_simplejwt.views import TokenRefreshView
from process.views import  ForestLetterDetail, ForestLetterList, RegionDetail, RegionList, RetrieveGenNum, UserDetail, UserLevelDetail, UserLevelList, UserList
from django.urls import path

urlpatterns = [
      
    path('region/', RegionDetail.as_view()),
    path('region/<int:pk>/', RegionList.as_view()),
    
    path('userlevel/', UserLevelDetail.as_view()),
    path('userlevel/<int:pk>/', UserLevelList.as_view()),
    
    path('userdetail/', UserDetail.as_view()),
    path('userdetail/<int:pk>/', UserList.as_view()),
    
    path('forestletter/', ForestLetterDetail.as_view()),
    path('forestletter/<int:pk>/', ForestLetterList.as_view()),
    
    path('genNum/', RetrieveGenNum.as_view()),
    

    ]