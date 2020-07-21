from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    event_name = models.TextField("Event Name", help_text = "The tile of the event")
    event_location = models.TextField("Event Location", help_text = "The location of the event")
    start_day = models.DateField('Event date', help_text='The date the event will be on')
    end_day = models.DateField('Event date', help_text='The date the event will be on', default = start_day)
    start_time = models.TimeField('Starting time', help_text='The time the event will start')
    end_time = models.TimeField('Final time', help_text='The time the event will end')
    _user = models.ForeignKey(User, on_delete = models.CASCADE)
