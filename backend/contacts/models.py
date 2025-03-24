from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Relation(models.Model):
    title = models.CharField(max_length=50, unique=True)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.title


class Contact(models.Model):
    CONTACT_TYPE_CHOICES = (
        ('family', "Family"),
        ('friend', "Friend"),
        ('colleague', "Colleague"),
        ('classmate', "Classmate"),
        ('neighbor', "Neighbor"),
        ('acquaintance', "Acquaintance"),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=7, choices=CONTACT_TYPE_CHOICES)
    user = models.ForeignKey( User, on_delete=models.CASCADE, related_name='contacts' ) # user.contacts.all() 
    relation = models.ForeignKey(Relation, on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        unique_together = ('user', 'email')
        ordering = ['-created_at']
        verbose_name_plural = "Contacts"

    def __str__(self) -> str:
        return f"{self.name} <{self.email}>"