from django.urls import path

from .views import WireDamageDetectionCreateView, WireDamageDetectionListView

app_name = 'wire'

urlpatterns = [
    path("create/", WireDamageDetectionCreateView.as_view(), name="wire_create"),
    path("list/", WireDamageDetectionListView.as_view(), name="wire_list"),
]
