from django.urls import path

from apps.flight.views import FlightListView


app_name = 'flight'


urlpatterns = [
    path('list/', FlightListView.as_view(), name='flight_list'),
]
