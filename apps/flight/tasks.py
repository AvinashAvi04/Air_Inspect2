from __future__ import absolute_import, unicode_literals

import re
import uuid
import logging

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task()
def ingest_data(ingest_id):
    pass

