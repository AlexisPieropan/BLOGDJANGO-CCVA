from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'address', 'dni')
    fieldsets = (
        *UserAdmin.fieldsets,  
        (                      
            'Información adicional',  
            {
                'fields': (
                    'address',
                    'dni',
                    'role',
                )
            }
        )           )

admin.site.register(User, CustomUserAdmin)
