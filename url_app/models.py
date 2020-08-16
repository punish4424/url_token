from django.contrib.postgres.fields import JSONField
from django.db import models


class Token(models.Model):
    token = models.CharField(max_length=50)
    data = JSONField()
    used = models.BooleanField(default=False)

    def __str__(self):
        return self.token

    class Meta:
        verbose_name = 'Token'
        verbose_name_plural = 'Tokens'
