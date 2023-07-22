from django.db import models


class Quotation(models.Model):
  customer_id = models.CharField(max_length=255)
  item_bought = models.JSONField(default=list)
  order_count = models.JSONField(default=dict)
  
  

