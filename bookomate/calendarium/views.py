from datetime import datetime
from django.shortcuts import render, redirect
from .calendar import EventCalendar
from .models import Event
from .forms import EventForm
from django.utils.safestring import mark_safe


def home(request):
    return redirect('calendar_view')


def calendar_view(request, year: int = None, month: int = None):
    if year is None or month is None:
        _now = datetime.now()
        year, month = _now.year, _now.month

    _calendar = EventCalendar()
    _now = datetime.now()
    html = _calendar.formatmonth(theyear=year, themonth=month, withyear=True)
    html = html.replace('<td ', '<td  width="250" height="200"')
    prev_year = year
    next_year = year
    prev_month = month - 1
    next_month = month + 1
    if month == 12:
        next_year = next_year + 1
        next_month = 1
    elif month == 1:
        prev_year = prev_year - 1
        prev_month = 12
    params = {"calendar": mark_safe(html), "next_year": next_year, "prev_year": prev_year, "next_month": next_month, "prev_month": prev_month}
    return render(request, "calendarium/calendar.html", params)

def event_creation_view(request):
    if request.method == "GET":
        event = Event.objects.get(pk = 1)
        form = EventForm(instance = event)
        params = {"form": form}
        return render(request, "calendarium/eventCreation.html", params)
