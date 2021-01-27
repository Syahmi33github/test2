from django.contrib import admin

from .models import PostModels

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['slug',
    ]
    
admin.site.register(PostModels, PostAdmin)