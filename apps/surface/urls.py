from django.urls import path

from .views import SurfaceDamageDetectionCreateView, SurfaceDamageDetectionListView, SurfaceDamageDetectionDetailView

app_name = "surface"

urlpatterns = [
    path("create/<int:id>/", SurfaceDamageDetectionCreateView.as_view(), name="damage_create"),
    path("list/", SurfaceDamageDetectionListView.as_view(), name="damage_list"),
    path("detail/<int:id>/", SurfaceDamageDetectionDetailView.as_view(), name="damage_detial"),
]
