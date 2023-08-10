from django.contrib.auth.models import User

from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from django.db import connection
# from Harvesting.process.models import ScheduleItems


from process.models import CoupWorkProgram,ForestLetter, ForestUser, LetterTemplate, LetterToRM, Region, UserLevel, ScheduleItems, Schedule, Post

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

class CoupWorkProgramSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = CoupWorkProgram
        fields = ('__all__')                        
        expandable_fields = {'ForestLetter': (ForestletterSerializer, {'source': 'id', 'fields': ['my_ref', 'title', 'letter_url']}),}

class LetterToRMSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = LetterToRM
        fields = ('__all__')                        
        expandable_fields = {'ForestLetter': (ForestletterSerializer, {'source': 'id', 'fields': ['my_ref', 'title', 'letter_url']}),}
        
class LetterTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LetterTemplate
        fields = ('__all__')
        
class ScheduleItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleItems
        fields = ('__all__')
        
class ScheduleSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Schedule
        fields = ('__all__')                        
        expandable_fields = {'ScheduleItems': (ScheduleItemsSerializer, {'source': 'item_id', 'fields': ['item_text', 'item_order', 'item_enabled']}),}
        
# this is for get the laste id number from the database (this is working fine)
class NumGenSerializer(serializers.ModelSerializer):
    # Serializer fields and configurations
    def get_last_inserted_row_number(self):
        try:
            last_instance = ForestLetter.objects.latest('id')
            return last_instance.id
        except ForestLetter.DoesNotExist:
            # Handle the case where no instances of ForestLetter exist
            # or the table is empty
            return 0
        except Exception as e:
            # Handle other exceptions that might occur during the operation
            # Log the error or perform any necessary error handling
            print(f"An error occurred: {str(e)}")
            return None
    
# file upload 

class PostViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('__all__')

""" 
Extend user and autohnticatons

"""

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password  = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        
        user.set_password(validated_data['password'])
        user.save()

        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    password  = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.set_password(validated_data['password'])
        instance.save()

        return instance

class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value

    def update(self, instance, validated_data):
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.username = validated_data['username']

        instance.save()

        return instance

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.username = validated_data['username']

        instance.save()

        return instance
