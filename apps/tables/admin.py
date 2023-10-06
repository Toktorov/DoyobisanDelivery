from django.contrib import admin

from apps.tables.models import Table

# Register your models here.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('title', 'number', 'created')