from django.contrib import admin
from signup.models import USER

class UserAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','sex','email','password')

admin.site.register(USER,UserAdmin)