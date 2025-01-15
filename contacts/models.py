from django.db import models
from django.urls import reverse


# Create your models here.
class Contact(models.Model):
    first_name = models.TextField(max_length=200, default="")
    last_name = models.TextField(max_length=200, default="")

    #CHOICES for sex
    SEX_CHOICES = (
        ("M", "Male"),
        ("F", "Female")
    )
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES)

    nationality = models.TextField(max_length=200, default="")
    email = models.TextField(max_length=500, default="")
    job = models.TextField(max_length=200, default="")
    experience = models.IntegerField(default=0)
    birthday = models.DateField(null=True)
    bio = models.TextField(
        default='TBA',
        max_length=2000
    )

    #REDIRECTS ON CONTACT CREATION
    def get_absolute_url(self):
        return reverse('contacts:view_contact', kwargs={'pk': self.pk})

    #STRING REPRESENTATION OF OBJECT
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
