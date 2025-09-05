from django.contrib import admin
from .models import ComingSoonPage

@admin.register(ComingSoonPage)
class ComingSoonPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'subtitle')
    fields = ('title', 'subtitle', 'on_air_text', 'background_image', 'is_active', 'logo')