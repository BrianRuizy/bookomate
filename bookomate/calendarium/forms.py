from models import Event
from django.forms import ModelForm

class EventForm():
    class Meta:
        model = Event
        fields = ['day', 'start time', 'end time']
