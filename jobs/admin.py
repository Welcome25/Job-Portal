from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'employment_type', 'posted_by', 'posted_at')
    list_filter = ('employment_type', 'location', 'company')
    search_fields = ('title', 'company', 'location', 'description')
