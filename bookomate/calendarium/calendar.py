from calendar import HTMLCalendar
from .models import Event


class EventCalendar(HTMLCalendar):
    def __init__(self, events=None):
        super(EventCalendar, self).__init__()
        self.events = events

    def formatday(self, day, weekday, events):
        """
        Return a day as a table cell.
        """
        events_from_day = events.filter(start_date__day=day)
        events_html = "<ul>"
        for event in events_from_day:
            events_html += f"{event.start_time} -- {event.end_time}" + "<br>"
        events_html += "</ul>"

        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # day outside month
        else:
            return '<td class="%s">%d%s</td>' % (self.cssclasses[weekday], day, events_html)

    def formatweek(self, theweek, events):
        """
        Return a complete week as a table row.
        """
        s = ''.join(self.formatday(d, wd, events) for (d, wd) in theweek)
        return '<tr>%s</tr>' % s

    def formatmonth(self, theyear, themonth, withyear=True):
        """
        Return a formatted month as a table.
        """

        events = Event.objects.filter(start_date__month=themonth)

        v = [
            '<table border="0" cellpadding="0" cellspacing="0" class="month">',
            '\n',
            self.formatmonthname(theyear, themonth, withyear=withyear),
            '\n',
            self.formatweekheader(),
            '\n'
        ]

        for week in self.monthdays2calendar(theyear, themonth):
            v.append(self.formatweek(week, events))
            v.append('\n')

        v.append('</table>')
        v.append('\n')
        return ''.join(v)
