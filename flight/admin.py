from decimal import getcontext
from django.contrib import admin
from . import models
from django.apps import apps
from .apps import FlightConfig


# register all models in `flight` app
app = apps.get_app_config("flight")
for model_name, model in app.models.items():
    admin.site.register(model)
