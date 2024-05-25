import os
from django.db.models.query import QuerySet
import requests
from gemini.get_faulty_wire import generate_gemini_response
from django.views import generic
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import WireFault
from config.settings import base
from apps.surface.models import SurfaceDamage
from apps.flight.models import Flight
from apps.utils.utils import SideBarSelectedMixin
import PIL.Image
import time
class WireDamageDetectionCreateView(
    LoginRequiredMixin, SideBarSelectedMixin, generic.TemplateView
):
    template_name = "pages/faulty_wire/input_wire_fault.html"
    parent = "faulty_wire_detection"
    segment = "wire_input"
    def post(self, request, **kwargs):
        print("BADO BADI")
        image = request.FILES.get("image")
        if not image:
            return JsonResponse({"error": "No image file provided."}, status=400)
        base_dir = os.path.join(base.MEDIA_ROOT, "wire")
        os.makedirs(base_dir, exist_ok=True)
        image_path = os.path.join(base_dir, image.name)
        try:
            with open(image_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)
        except Exception as e:
            print(e)
            return JsonResponse({"error": "Failed to process image.", "details": str(e)}, status=500)

        time.sleep(5)
        print("AAi haye")
        try:
            print(image_path)
            img = PIL.Image.open(image_path)
            result = generate_gemini_response(img)
            print(result)
            print("OOe hoye")
            print(result)
            WireFault.objects.create(
                fault_detected=result['Fault_Detected'],
                component_name=result['Component_Name'],
                fault=result['Fault'],
                description=result['Description'],
                raw=result
            )
            return JsonResponse(result)
        except Exception as e:
            print(e)
            return JsonResponse({"error": "Failed to process image.", "details": str(e)}, status=500)


class WireDamageDetectionListView(LoginRequiredMixin, generic.ListView):
    model = WireFault
    template_name = "pages/faulty_wire/wire_fault_report.html"
    context_object_name = "wire_fault_list"

    def get_queryset(self):
        return WireFault.objects.all()  