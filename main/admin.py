from django.contrib import admin
from .models import SimplePost
@admin.register(SimplePost)
class SimplePostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title','created_at','published')
