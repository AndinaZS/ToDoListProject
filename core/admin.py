from django.contrib import admin
from core.models import User



class AdminUser(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    fields = ['username', 'first_name', 'last_name',
              'email', 'is_active', 'is_staff', 'date_joined', 'last_login']
    readonly_fields =['date_joined', 'last_login']


admin.site.register(User, AdminUser)