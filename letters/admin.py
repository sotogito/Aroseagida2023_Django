from django.contrib import admin
from .models import PrevLetter, Comment




class PrevLetterAdmin(admin.ModelAdmin):
    list_display = ['id','question_type','level_type','question','option','question_text','is_active']
    search_fields = ['question_text']


admin.site.register(PrevLetter, PrevLetterAdmin)
admin.site.register(Comment)








