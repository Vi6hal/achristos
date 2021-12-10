from django.contrib import admin
from .models import AppRegistery


@admin.register(AppRegistery)
class AppRegisteryAdmin(admin.ModelAdmin):
    list_display = ('url', 'last_pinged', 'bedtime')
    def bedtime(self):
        return bool(self.bedtime)
    bedtime.boolean = True
    fieldsets = [
        (None,               {'fields': ['url']}),
        ('Other information', {'fields': ['last_pinged','bedtime'], 'classes': ['collapse']}),
        ('Meta', {'fields': ['created_by','created_at','updated_at','updated_by'], 'classes': ['collapse']}),
    ]
    readonly_fields=['created_by','created_at','updated_at','updated_by']
