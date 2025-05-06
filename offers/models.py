from django.db import models

class Offer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
