from datetime import datetime
from django.shortcuts import render, redirect
from .calendar import EventCalendar
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
    params = {"calendar": mark_safe(html), "year": year, "next_month": month + 1, "prev_month": month - 1}
    return render(request, "calendarium/calendar.html", params)
