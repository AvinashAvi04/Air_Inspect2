import os
from django.db.models.query import QuerySet
import requests

from django.views import generic
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from config.settings import base
from apps.surface.models import SurfaceDamage
from apps.flight.models import Flight
from apps.utils.utils import SideBarSelectedMixin


ROBOFLOW_API_URL = "https://detect.roboflow.com"
ROBOFLOW_API_KEY = "sa2EK72jNNj3XtZlIcUl"
ROBOFLOW_MODEL_ID = "aircraft-damage-detection-2/3"


def analyze_image(image_path):
    url = f"{ROBOFLOW_API_URL}/{ROBOFLOW_MODEL_ID}?api_key={ROBOFLOW_API_KEY}"
    with open(image_path, 'rb') as file:
        response = requests.post(url, files={"file": file})
    return response.json()


class SurfaceDamageDetectionCreateView(
    LoginRequiredMixin, SideBarSelectedMixin, generic.TemplateView
):
    template_name = "pages/surface_damage/input_surface_damage.html"
    parent = "surface_detection"
    segment = "surface_input"

    def post(self, request, **kwargs):
        id = kwargs.get("id")
        print(id)
        print("BADO BADI")
        image = request.FILES.get("image")
        if not image:
            return JsonResponse({"error": "No image file provided."}, status=400)

        base_dir = os.path.join(base.MEDIA_ROOT, "surface_damage")
        os.makedirs(base_dir, exist_ok=True)
        image_path = os.path.join(base_dir, image.name)
        print("AAi haye")
        try:
            with open(image_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)
            result = analyze_image(image_path)
            print(result)
            print("OOe hoye")
            print(result)
            for pred in result.get("predictions"):
                SurfaceDamage.objects.create(
                    flight_id=id,
                    damage_type=pred.get("class"),
                    level=str(pred.get("confidence")),
                    image=image,
                    metadata=pred
                )
            return JsonResponse(result)
        except Exception as e:
            print(e)
            return JsonResponse({"error": "Failed to process image.", "details": str(e)}, status=500)


class SurfaceDamageDetectionListView(
    LoginRequiredMixin, SideBarSelectedMixin, generic.ListView
):
    model = Flight
    template_name = "pages/surface_damage/surface_damage_reports.html"
    context_object_name = "surface_damage_list"
    parent = "surface_detection"
    segment = "surface_report"
    paginate_by = 6


class SurfaceDamageDetectionDetailView(
    LoginRequiredMixin, SideBarSelectedMixin, generic.ListView
):
    model = SurfaceDamage
    template_name = "pages/surface_damage/report.html"
    context_object_name = "surface_damage_list"
    parent = "surface_detection"
    segment = "surface_report"
    paginate_by = 6

    def get_queryset(self):
        queryset =  super().get_queryset()
        id = self.kwargs.get("id")
        fd = Flight.objects.get(id=id)
        return queryset.filter(flight_id=fd.id)
