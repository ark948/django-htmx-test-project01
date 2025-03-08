from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    published = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title