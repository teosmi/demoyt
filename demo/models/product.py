from django.db import models

class product(models.Model):
       
    name            = models.CharField(max_length=30)
    status          = models.CharField(max_length=10, null=True)

    def __str__ (self):
        return f"{self.name}"