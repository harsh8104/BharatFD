# faq/admin.py

from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'question_hi', 'question_bn', 'answer', 'answer_hi', 'answer_bn']
    search_fields = ['question', 'question_hi', 'question_bn']
    list_filter = ['question', 'question_hi', 'question_bn']