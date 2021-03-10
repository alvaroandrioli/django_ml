from sys import version
from django.db import models
from django.db.models import base

# Create your models here.
class Endpoint(models.Model):
  '''
  Objeto que representa um endpoint de para os algoritmos
  '''
  name = models.CharField(max_length=128)
  owner = models.CharField(max_length=128)
  created_at = models.DateTimeField(auto_now_add=True, blank=True)

class MLAlgorithm(models.Model):
  '''
  Objeto que representa o algoritmo de ML
  '''
  name = models.CharField(max_length=128)
  description = models.CharField(max_length=128)
  code = models.CharField(max_length=50000)
  version = models.CharField(max_length=128)
  woner = models.CharField(max_length=128)
  creadted_app = models.DateTimeField(auto_now_add=True, blank=True)
  parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)

class MLAlgorithmStatus(models.Model):
  '''
  Objeto que representa o status MLAlgorithm, este status pode mudar durante o tempo
  '''
  status = models.CharField(max_length=128)
  active = models.BooleanField()
  created_by = models.CharField(max_length=128)
  created_at = models.DateTimeField(auto_now_add=True, blank=True)
  parent_mlalgorithm = models.ForeignKey(
    MLAlgorithm, 
    on_delete=models.CASCADE, 
    related_name = "status")

class MLRequest(models.Model):
  '''
  Objeto que manterá todos os dados de requisição para os modelos de ML.
  '''
  input_data = models.CharField(max_length=10000)
  full_response = models.CharField(max_length=10000)
  response = models.CharField(max_length=10000)
  feedback = models.CharField(max_length=10000, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True, blank=True)
  parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE)