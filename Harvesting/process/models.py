from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Region(models.Model):
    region_id      = models.AutoField(primary_key=True)
    region_txt     = models.CharField(max_length=200, default=None, blank=True, null=True)
    region_code    = models.CharField(max_length=10, default=None, blank=True, null=True)
    region_status  = models.IntegerField(default=None, blank=True, null=True)
# admin panel show this below data
    def __str__(self):
        #return self.region_txt,self.region_code,self.region_id
        #return '%s %s'%(self.region_txt,self.region_code)
        return '{} {} {} '.format(self.region_txt,self.region_code,self.region_id)

class UserLevel(models.Model):
    level_id              = models.AutoField(primary_key=True)
    level_name            = models.CharField(max_length=100, default=None, blank=True, null=True)
    avalableUserLevel     = models.BooleanField(default=True)
# admin panel show this below data
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
# admin panel show this below data
    def __str__(self):
        return '{} {}  '.format(self.User,self.account_status)

class ForestLetter(models.Model):
    id             = models.AutoField(primary_key=True)
    system_no      = models.CharField(max_length=200, default=None, blank=True, null=True) 
    my_ref         = models.CharField(max_length=200,unique =True)
    title          = models.CharField(max_length=200, default=None, blank=True, null=True)
    issued_date    = models.DateField( default=None, blank=True, null=True)
    letter_url     = models.CharField(max_length=200, default=None, blank=True, null=True)
    received_date  = models.DateField( default=None, blank=True, null=True)
    added_date     = models.DateField( default=None, blank=True, null=True)
    # entered_user   = models.ForeignKey(UserLevel, to_field='level_id',   related_name="level_id_list" ,  on_delete=models.CASCADE) 
    entered_user   = models.CharField(max_length=200, default=None, blank=True, null=True) 
    original_excel = models.FileField(max_length=200, default=None, blank=True, null=True)
    
# admin panel show this below data
    def __str__(self):
        return '{} {} {} {} '.format(self.my_ref, self.title, self.letter_url, self.received_date)

class CoupWorkProgram(models.Model):
    id             = models.AutoField(primary_key=True)
    forest_ref     = models.CharField(max_length=200,unique =True)
    region         = models.CharField(max_length=200, default=None, blank=True, null=True)
    beat           = models.CharField(max_length=200, default=None, blank=True, null=True)
    d_s_d          = models.CharField(max_length=200, default=None, blank=True, null=True)
    g_s_d          = models.CharField(max_length=200, default=None, blank=True, null=True)
    village        = models.CharField(max_length=200, default=None, blank=True, null=True)
    b_s_d          = models.CharField(max_length=200, default=None, blank=True, null=True)
    extent         = models.CharField(max_length=200, default=None, blank=True, null=True)
    present_sp     = models.CharField(max_length=200, default=None, blank=True, null=True)
    plant_sp       = models.CharField(max_length=200, default=None, blank=True, null=True)
    enter_date     = models.DateField( default=None, blank=True, null=True)
    entered_user   = models.CharField(max_length=200, default=None, blank=True, null=True) 
    
    forest_id      = models.ForeignKey(ForestLetter, to_field='id',   related_name="forest_Id" ,  on_delete=models.CASCADE)
# admin panel show this below data
    def __str__(self):
        return '{} {} {} {}'.format(self.forest_ref,self.region,self.village,self.enter_date)
    
class LetterToRM(models.Model):
    id             = models.AutoField(primary_key=True)
    letter_date    = models.DateField( default=None, blank=True, null=True)
    form_ref_no    = models.CharField(max_length=200,unique =True)
    full_letter    = models.CharField(max_length=10000, default=None, blank=True, null=True) 
    letter_my_no   = models.CharField(max_length=200,unique =True)
    
    form_id        = models.ForeignKey(ForestLetter, to_field='id',   related_name="letter_to_rm_Id" ,  on_delete=models.CASCADE)
# admin panel show this below data
    def __str__(self):
        return '{} {} {}'.format(self.form_id, self.form_ref_no, self.letter_my_no)   
    
     
class LetterTemplate(models.Model):
    id             = models.AutoField(primary_key=True)
    template_id    = models.CharField(max_length=200,unique =True)
    template_text  = models.CharField(max_length=10000, default=None, blank=True, null=True) 
    # form_id        = models.ForeignKey(ForestLetter, to_field='id',   related_name="letter_to_rm_Id" ,  on_delete=models.CASCADE)
    
# admin panel show this below data
    def __str__(self):
        return '{} {}'.format(self.template_id, self.template_text)    
    
class ScheduleItems(models.Model):
    item_id        = models.AutoField(primary_key=True)
    item_text      = models.CharField(max_length=10000, default=None, blank=True, null=True) 
    item_order     = models.IntegerField(default=None, blank=True, null=True) 
    item_enabled   = models.BooleanField(max_length=100, default=None, blank=True, null=True)   
    
# admin panel show this below data
    def __str__(self):
        return '{} {} {}'.format(self.item_text, self.item_order, self.item_enabled)   


class Schedule(models.Model):
    schedule_id    = models.AutoField(primary_key=True)
    no_of_dates    = models.IntegerField(default=None, blank=True, null=True)
    from_date      = models.DateField( default=None, blank=True, null=True) 
    to_date        = models.DateField( default=None, blank=True, null=True)  
    
    item_id        = models.ForeignKey(ScheduleItems, to_field='item_id', related_name="schedule_items_reference" , on_delete=models.CASCADE)

    
# admin panel show this below data
    def __str__(self):
        return '{} {} {}'.format(self.no_of_dates, self.from_date, self.to_date)   
    

class Post(models.Model):
    document = models.FileField(null=True, blank=True)