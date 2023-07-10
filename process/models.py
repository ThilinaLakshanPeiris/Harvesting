from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Region(models.Model):
    region_id      = models.AutoField(primary_key=True)
    region_txt     = models.CharField(max_length=200, default=None, blank=True, null=True)
    region_code    = models.CharField(max_length=10, default=None, blank=True, null=True)
    region_status  = models.IntegerField(default=None, blank=True, null=True)
    def __str__(self):
        #return self.region_txt,self.region_code,self.region_id
        #return '%s %s'%(self.region_txt,self.region_code)
        return '{} {} {} '.format(self.region_txt,self.region_code,self.region_id)

class UserLevel(models.Model):
    level_id              = models.AutoField(primary_key=True)
    level_name            = models.CharField(max_length=100, default=None, blank=True, null=True)
    avalableUserLevel     = models.BooleanField(default=True)
    
    def __str__(self):
        return self.level_name

class ForestUser(models.Model):
    User            = models.OneToOneField(User, on_delete=models.CASCADE)
    forest_user_id  = models.AutoField(primary_key=True)
    account_status 	= models.BooleanField(default=True)
    last_login_time	= models.DateTimeField(auto_now=True) 
    contact_no      = models.IntegerField( default=None, blank=True, null=True)
    region_id       = models.ForeignKey(Region, to_field='region_id',   related_name="region_id_list" ,  on_delete=models.CASCADE) 
    level_id        = models.ForeignKey(UserLevel, to_field='level_id', related_name="users_level_list", on_delete=models.CASCADE) 

    def __str__(self):
        return '{} {}  '.format(self.User,self.account_status)

class ForestLetter(models.Model):
    id             = models.AutoField(primary_key=True)
    system_no      = models.CharField(max_length=200, default=None, blank=True, null=True) 
    my_ref         = models.CharField(max_length=200,unique =True)
    title          = models.CharField(max_length=200, default=None, blank=True, null=True)
    issued_date    = models.DateTimeField( default=None, blank=True, null=True)
    letter_url     = models.CharField(max_length=200, default=None, blank=True, null=True)
    received_date  = models.DateTimeField( default=None, blank=True, null=True)
    added_date     = models.DateTimeField( default=None, blank=True, null=True)
    # entered_user   = models.ForeignKey(UserLevel, to_field='level_id',   related_name="level_id_list" ,  on_delete=models.CASCADE) 
    entered_user   = models.CharField(max_length=200, default=None, blank=True, null=True) 
    original_excel = models.CharField(max_length=200, default=None, blank=True, null=True)
    
    def __str__(self):
        return '{} {} {} {} {}'.format(self.title,self.issued_date,self.letter_url,self.received_date,self.entered_user)

