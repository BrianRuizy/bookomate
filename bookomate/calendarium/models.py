from django.db import models


class Event(models.Model):
    day = models.DateField('Event date', help_text='Event date')
    start_time = models.TimeField('Starting time', help_text='Starting time')
    end_time = models.TimeField('Final time', help_text='Final time')
