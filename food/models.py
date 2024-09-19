from django.db import models

class Item(models.Model): 
   def __str__(self) -> str:
       return self.item_name
   item_name = models.CharField(max_length=200)
   item_desc = models.CharField(max_length=200)
   item_price = models.IntegerField()