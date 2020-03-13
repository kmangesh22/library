from django.db import models

# Create your models here.

class Author(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 200, unique = True)

    def __str__(self):
        return f"{self.id} - {self.name}"


class Book(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 200, unique = True)
    price = models.FloatField(null=False)
    description = models.TextField(null=False)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name="books")

    def __str__(self):
        return f"{self.id} - {self.name}"



