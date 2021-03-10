"""
WSGI config for ml project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'servier.settings')

application = get_wsgi_application()

import inspect
from apps.ml.registry import MLRegistry
from apps.ml.income_classifier.random_forest import RandomForestClassifier

try:
  registry = MLRegistry()
  rf = RandomForestClassifier()
  registry.add_algorithm(
    endpoint_name="income_classifier",
    algorithm_object=rf,
    algorithm_name="random forest",
    algorithm_status="develop",
    algorithm_version="0.0.1",
    owner="andrioli",
    algorithm_description="Classificador random forest",
    algorithm_code=inspect.getsource(RandomForestClassifier)
  )
except Exception as e:
  print("erro ao carregar o algoritmo " + e)
