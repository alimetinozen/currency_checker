from django.urls import reverse
from django.db.models import CharField
from django.db.models import DateTimeField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models


class Provider(models.Model):
    # Fields
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.pk
