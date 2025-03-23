from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Relation(models.Model):
    RELATION_TITLE_CHOICES = (
        ('family', "Family"),
        ('friend', "Friend"),
        ('colleague', "Colleague"),
        ('classmate', "Classmate"),
        ('neighbor', "Neighbor"),
        ('acquaintance', "Acquaintance"),
    )

    title = models.CharField(max_length=12, choices=RELATION_TITLE_CHOICES)

    def __str__(self) -> str:
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey( User, on_delete=models.CASCADE, related_name='contacts' ) # user.contacts.all() 
    relation = models.ForeignKey(Relation, on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        unique_together = ('user', 'email')
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f"{self.name} <{self.email}>"