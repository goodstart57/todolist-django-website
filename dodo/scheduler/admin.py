from django.contrib import admin
from .models import Schedule, Label
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User


# class ProfileInline(admin.StackedInline):
# 	model = Profile
# 	can_delete = False
# 	verbose_name_plural = 'profile'

# class UserAdmin(BaseUserAdmin):
# 	inlines = (ProfileInline, )

admin.site.register(Schedule)
admin.site.register(Label)
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
# admin.site.register(TodayStockOfUser)