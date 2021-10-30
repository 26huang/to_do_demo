from django.contrib import admin
from .models import Task

# Register your models here.

@admin.register(Task)
class ObjectTask(admin.ModelAdmin):
    fields = ('title', 'completed')

    list_display = ('id', 'title', 'completed')
    list_editable = ('completed',)