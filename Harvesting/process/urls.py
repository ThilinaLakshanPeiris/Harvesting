from rest_framework_simplejwt.views import TokenRefreshView
from process.views import ChangePasswordView, ForestLetterDetail, ForestLetterList, LetterTemplateDetail, \
    LetterTemplateList, LetterToRMDetail, LetterToRMList, LogoutAllView, LogoutView, MyObtainTokenPairView, RegionDetail, RegionList, RegisterView, UpdateProfileView, UserDetail, \
    UserLevelDetail, UserLevelList, UserList, coupWorkProgramDetail, coupWorkProgramList, ScheduleItemsList, \
    ScheduleItemsDetail, ScheduleList, ScheduleDetail, get_last_inserted_row_number, PostViewSet
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

    path('cwp/', coupWorkProgramDetail.as_view()),
    path('cwp/<int:pk>/', coupWorkProgramList.as_view()),

    path('lettertoRM/', LetterToRMDetail.as_view()),
    path('lettertoRM/<int:pk>/', LetterToRMList.as_view()),

    path('letterTemplate/', LetterTemplateDetail.as_view()),
    path('letterTemplate/<int:pk>/', LetterTemplateList.as_view()),

    path('scheduleItems/', ScheduleItemsDetail.as_view()),
    path('scheduleItems/<int:pk>/', ScheduleItemsList.as_view()),

    path('schedule/', ScheduleDetail.as_view()),
    path('schedule/<int:pk>/', ScheduleList.as_view()),

    path('lastrowid/', get_last_inserted_row_number, name='last-inserted-row'),


    path('postdata/', PostViewSet.as_view()),


    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(),
         name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(),
         name='auth_update_profile'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),

    # Other URL patterns


]
