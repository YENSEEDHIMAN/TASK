from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from regform.models import User

class UserModelAdmin(BaseUserAdmin):
    list_display = ["id", "email", "full_name", "dob", "is_staff", "is_superuser"] 
    list_filter = ["is_staff", "is_superuser"] 

    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["dob", "full_name", "gender", "phone_number", "address", "profile_picture"]}),  
        ("Permissions", {"fields": ["is_active", "is_staff", "is_superuser"]}),  
    ]
    APPEND_SLASH = False
    
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "full_name", "dob", "password1", "password2"],
            },
        ),
    ]

    search_fields = ["email", "full_name"]
    ordering = ["email", "id"]
    filter_horizontal = []

admin.site.register(User, UserModelAdmin)


