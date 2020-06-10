from datetime import datetime
from django.shortcuts import render
from .calendar import EventCalendar
from django.utils.safestring import mark_safe


def calendar_view(request):
    _calendar = EventCalendar()
    _now = datetime.now()
    html = _calendar.formatmonth(theyear=_now.year, themonth=_now.month, withyear=True)
    html = html.replace('<td ', '<td  width="250" height="200"')
    return render(request, "calendarium/calendar.html", {"calendar": mark_safe(html)})
