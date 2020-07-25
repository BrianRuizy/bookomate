from .models import Event
from django.forms import ModelForm, DateField
from datetime import date
from django.utils import dateparse
TIME_FORMAT = '%d.%m.%Y'

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_location',
              'start_date', 'start_time', 'end_time']

    def clean_start_date(self):
        data = self.data['start_date']
        return dateparse.parse_date(data)
