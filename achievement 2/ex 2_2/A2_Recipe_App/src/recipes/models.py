from django.db import models

# Create your models here.
class Recipes(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=250)
    id = models.PositiveBigIntegerField(primary_key=True)
    cooking_time = models.IntegerField()
    difficulty = models.CharField(max_length=20)
    
    def _str_(self):
        str(self.name)
        str(self.ingredients)
        str(self.id)
        str(self.cooking_time)
        str(self.difficulty)