from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.utils.utils import SideBarSelectedMixin
# from apps.wire.models import WireData


class WireDamageDetectionCreateView(
    LoginRequiredMixin, SideBarSelectedMixin, generic.TemplateView
):
    template_name = "pages/faulty_wire/input_wire_fault.html"
    parent = "faulty_wire_detection"
    segment = "wire_input"


class WireDamageDetectionListView(
    LoginRequiredMixin, SideBarSelectedMixin, generic.TemplateView
):
    # model = WireData
    template_name = "pages/faulty_wire/wire_fault_report.html"
    context_object_name = "surface_damage_list"
    parent = "faulty_wire_detection"
    segment = "faulty_wire_report"
    paginate_by = 6
