from django.contrib import admin
from .models import Data

class AdminChanges(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('created', 'countryName', 'coronaPositive','death',)

admin.site.register(Data,AdminChanges)

