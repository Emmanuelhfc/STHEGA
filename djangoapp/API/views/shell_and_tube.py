from API.serializers import *
from rest_framework import viewsets
from django.http import FileResponse, Http404
import io
import os
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['HEAT EXCHANGE AVALIATION'])
class ShellAndTubeAvaliation(viewsets.ViewSet):
    ...
