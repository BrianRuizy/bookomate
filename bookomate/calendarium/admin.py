from django.contrib import admin

from bookomate.calendarium.models import Event


class EventAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
