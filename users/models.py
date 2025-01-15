from django.db import models
from django.urls import reverse


# Create your models here.
class User(models.Model):
    password = models.TextField(max_length=200, default="")
    first_name = models.TextField(max_length=200, default="")
    last_name = models.TextField(max_length=200, default="")

    # CHOICES for sex
    SEX_CHOICES = (
        ("M", "Male"),
        ("F", "Female")
    )
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES)

    nationality = models.TextField(max_length=200, default="")
    email = models.TextField(max_length=500, default="")
    birthday = models.DateField(null=True)


    # REDIRECTS ON CONTACT CREATION
    def get_absolute_url(self):
        return reverse('user:view_user', kwargs={'pk': self.pk})

    # STRING REPRESENTATION OF OBJECT
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
