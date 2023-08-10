from django.contrib import admin

from process.models import CoupWorkProgram, ForestLetter, ForestUser, \
    LetterToRM, Region, UserLevel, LetterTemplate, ScheduleItems, Schedule, Post

# Register your models here.
class ForestUseInline(admin.StackedInline):
    model        = ForestUser
    can_delete   = False
    verbose_name = 'Fuel User'
    
admin.site.register(ForestUser)
admin.site.register(UserLevel)
admin.site.register(Region)
admin.site.register(ForestLetter)
admin.site.register(CoupWorkProgram)
admin.site.register(LetterToRM)
admin.site.register(LetterTemplate)
admin.site.register(ScheduleItems)
admin.site.register(Schedule)
admin.site.register(Post)
