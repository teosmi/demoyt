from django.db import models

class application(models.Model):
    
    product_id      = models.IntegerField()
    indication_id   = models.IntegerField()
    number          = models.CharField(max_length=6)
    name            = models.CharField(max_length=30)
    region          = models.CharField(max_length=10)
    type            = models.CharField(max_length=60)
    created_at      = models.DateField()
    status          = models.CharField(max_length=10, null=True)

    def __str__ (self):
        return f"{self.name}"


    
   
