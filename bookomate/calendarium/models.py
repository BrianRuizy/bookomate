from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AnonymousUser


def one_hour_after():
    return timezone.now() + timezone.timedelta(hours=1)

class Event(models.Model):
    event_name = models.TextField("Event Name", help_text = "The tile of the event", default="")
    event_location = models.TextField("Event Location", help_text = "The location of the event", default="")
    start_date = models.DateField('Event date', help_text='The date the event will be on', default=timezone.now)
    end_date = models.DateField('Event date', help_text='The date the event will be on', default=timezone.now)
    start_time = models.TimeField('Starting time', help_text='The time the event will start', default=timezone.now)
    end_time = models.TimeField('Final time', help_text='The time the event will end', default = one_hour_after())
    _user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, on_delete=models.CASCADE)

    @staticmethod
    def one_hour():
        return timezone.now() + timezone.timedelta(days=1)
