from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.utils.utils import SideBarSelectedMixin
from apps.flight.models import Flight


class FlightListView(LoginRequiredMixin, SideBarSelectedMixin, generic.TemplateView):
    template_name = "pages/integrations/data_ingestion/data_ingestion.html"
    parent = "ingest"
    segment = "ingest_data"
