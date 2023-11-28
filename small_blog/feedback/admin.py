from django.contrib import admin

from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'to_publish',
        'author',
        'created_at',
    )
    list_editable = (
        'to_publish',
    ) 
    list_filter = ('to_publish',)
    list_display_links = ('text',)

admin.site.register(Feedback, FeedbackAdmin)
