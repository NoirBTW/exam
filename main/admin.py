from django.contrib import admin
from .models import asexam

@admin.register(asexam)
class asexamAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'exam_date', 'is_public')
    search_fields = ('title', 'users__email')
    list_filter = ('is_public', 'created_at', 'exam_date')
    filter_horizontal = ('users',)
    date_hierarchy = 'exam_date'
