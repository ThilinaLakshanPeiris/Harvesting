from django.contrib import admin

from process.models import ForestUser, Region, UserLevel

# Register your models here.
class FuelUserInline(admin.StackedInline):
    model        = ForestUser
    can_delete   = False
    verbose_name = 'Fuel User'
    
admin.site.register(ForestUser)
admin.site.register(UserLevel)
admin.site.register(Region)