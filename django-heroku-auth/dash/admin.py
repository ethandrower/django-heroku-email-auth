from django.contrib import admin
#from django.contrib.auth.models import User

# Register your models here.

from .models import MyUser
#from django.contrib.auth.admin import UserAdmin



class UserAdmin(admin.ModelAdmin):

	list_display = ('email', 'username', 'approved')
	list_filter = ('email', 'approved')


#admin.site.unregister(User)
admin.site.register(MyUser, UserAdmin )