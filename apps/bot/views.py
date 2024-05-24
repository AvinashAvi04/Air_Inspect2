import json
import requests

from loguru import logger

from django.views import View
from django.views import generic
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.utils.utils import CSRFExemptMixin, SideBarSelectedMixin
from config.settings.local import TELEGRAM_API_URL, URL
from apps.bot.models import ConversationProcessing, Bot

from apps.bot.tasks import generate_and_send_response

class DamageDetection(
    LoginRequiredMixin, SideBarSelectedMixin, generic.ListView
):
    template_name = "pages/integrations/detection/damage.html"
    model = Bot
    context_object_name = "bot_list"
    success_url = "bot:bot_list"
    parent = "input"
    segment = "damageinput"
    paginate_by = 6

class DamageDetectionReports(
    LoginRequiredMixin, SideBarSelectedMixin, generic.ListView
):
    template_name = "pages/integrations/detection/damagereports.html"
    model = Bot
    context_object_name = "bot_list"
    success_url = "bot:bot_list"
    parent = "masterlist"
    segment = "damagemasterlist"
    paginate_by = 6





