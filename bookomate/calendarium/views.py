from calendar import HTMLCalendar

from django.shortcuts import render
from .calendar import EventCalendar
from django.utils.safestring import mark_safe


def calendar_view(request):
    _calendar = EventCalendar()
    return render(request, "calendarium/calendar.html", {"calendar": mark_safe(_calendar.formatmonth(2016, 5))})
