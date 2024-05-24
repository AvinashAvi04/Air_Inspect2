from django.urls import path

from .views import (

    DamageDetection,
    DamageDetectionReports
    

)

app_name = "bot"

urlpatterns = [
    path("detection", DamageDetection.as_view(), name="bot_list"),
    path("detection/damagereports", DamageDetectionReports.as_view(), name="damagereports"),
]
