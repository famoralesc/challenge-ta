from django.db import models
from challenge_app.constants import BAJA, MEDIA, ALTA

type_enum = (
    (BAJA, BAJA),
    (MEDIA, MEDIA),
    (ALTA, ALTA),
)

class Alerts(models.Model):
    id_alerta = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(unique=True)
    value = models.FloatField()
    version = models.IntegerField()
    type = models.TextField(choices=type_enum)
    sended = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    