from django.db import models

class Link(models.Model):
    def __str__(self):
        return self.name or self.address or "No Name"
    address = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)


