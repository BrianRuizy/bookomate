from datetime import datetime
from django.utils.dateparse import parse_date
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.edit import CreateView
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

def event_create(request):
    if request.method == "GET":
        form = EventForm()
        context = {"form": form}
        return render(request, "calendarium/event_form.html", context)
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event._user = request.user
            event.save()
