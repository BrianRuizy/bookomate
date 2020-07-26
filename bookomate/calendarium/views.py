from datetime import datetime
from django.utils.dateparse import parse_date
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, HttpResponseRedirect
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


def event_edit_create(request, pk=None, template="calendarium/event_form.html"):
    # Branch so that the form is not prepopulated (this is done by the managing javascript)
    if not pk and request.method == "GET":
        return render(request, template, {})
    if pk:
        event = get_object_or_404(Event, pk = pk)
        if event.user != request.user:
            return HttpResponseRedirect('/accounts/login', )
    else:
        event = Event(user = request.user)
    form = EventForm(request.POST or None, instance = event)

    if request.method == "POST" and form.is_valid():
        form.save()
    context = {"form": form}
    return render(request, "calendarium/event_form.html", context)


def event_delete(request, pk= None):
    if pk:
        event = get_object_or_404(Event, pk=pk)
        if event.user != request.user:
            return HttpResponseRedirect('/accounts/login', )
        event.delete()
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")

def event_list(request):
    if request.user.is_authenticated:
        context = {"events": Event.objects.filter(user=request.user)}
        return render(request, "calendarium/event_list.html", context)
    else: 
        return HttpResponseRedirect('/accounts/login', )
