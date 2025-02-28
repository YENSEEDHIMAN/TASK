from django.contrib import admin
from .models import Task  # Importing your Task model

# Register your Task model
admin.site.register(Task)

# Customizing Admin Panel Text for To-Do App
admin.site.site_header = "To-Do App Admin"
admin.site.site_title = "To-Do Admin Portal"
admin.site.index_title = "Welcome to the To-Do App Management Portal"