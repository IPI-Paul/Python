# Django Model Instance as an API Response =>
from django.db import models
# <= Django Model Instance as an API Response


class Product(models.Model):
  # Django Model Instance as an API Response =>
  # pk
  title = models.CharField(max_length=120)
  content = models.TextField(blank=True, null=True)
  price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
  # <= Django Model Instance as an API Response
