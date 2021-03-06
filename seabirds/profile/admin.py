from django import forms
from django.db import models
from django.contrib import admin
from profile.models import UserProfile, CollaborationChoice
from reversion.admin import VersionAdmin
from django.contrib.auth.models import User
from mptt.admin import MPTTModelAdmin

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'institution', 'country')
    list_filter = ('institution','country')
admin.site.register(UserProfile, UserProfileAdmin)

class CollaborationChoiceAdmin(admin.ModelAdmin):
    list_display = ('label',)
admin.site.register(CollaborationChoice, CollaborationChoiceAdmin)
