from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=30, unique=True, null=False)
    author = models.CharField(max_length=20, null=False)
    price = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.id} - {self.title} - {self.author} - {self.price}"
