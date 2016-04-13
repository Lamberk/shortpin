from django.contrib import admin

from .models import Key


class KeyAdmin(admin.ModelAdmin):


    model = Key
    fields = ('id', 'status', 'client')
    list_display = ('id', 'status')

admin.site.register(Key, KeyAdmin)
