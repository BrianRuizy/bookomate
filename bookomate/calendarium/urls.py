from django.urls import path

from . import views

urlpatterns = [
    # path('', views.home, name='home'), TODO: show calendar once user is authenticated
    path('calendar/', views.calendar_view, name='calendar_view'),
    path('calendar/<int:year>/<int:month>', views.calendar_view, name='calendar_view'),
    path('event/add/', views.event_edit_create, name = 'event_creation_view'),
    path('event/<int:pk>', views.event_edit_create, name='event-detail'),
    path('event/<int:pk>/delete', views.event_delete, name = "event_delete_view"),
    path('event/', views.event_list, name = "event_list_view"),

]
