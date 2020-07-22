from .models import Event
from django.forms import ModelForm, DateField
from datetime import date
TIME_FORMAT = '%d.%m.%Y'

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_location', 'start_date', 'start_time', 'end_time']
