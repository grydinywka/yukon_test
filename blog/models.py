from django.db import models
from django.conf import settings


class BlogPost(models.Model):
    name = models.CharField(max_length=100, null=True)
    text = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{id} - {name}".format(id=self.id, name=self.name)

