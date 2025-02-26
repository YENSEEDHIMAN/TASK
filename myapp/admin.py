from django.contrib import admin

# Register your models here.

from .models import Contact  # Replace with your model name

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')  # Replace with your model's fields
    search_fields = ('name', 'email', 'message')  # Optional: Fields to search in the admin panel

admin.site.register(Contact, YourModelAdmin)

