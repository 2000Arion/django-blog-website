from django.contrib import admin

from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("Titel", "slug", "Status", "Erstellt")
    list_filter = ("Status",)
    search_fields = ["Titel", "Inhalt"]

admin.site.register(Post, PostAdmin)
