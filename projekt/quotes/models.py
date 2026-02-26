from django.db import models
class Quote(models.Model):
    content = models.TextField(verbose_name="Treść cytatu")
    autor = models.CharField(max_length=200, verbose_name="Autor")
    date_added = models.DataTimeField()

    def __str__(self):
        return f"{self.author}: {self.content[:30]}..."
# Create your models here.
