from django.db import models


class AppModel(models.Model):
    title = models.CharField(
        max_length=255,
    )
