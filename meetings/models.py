from django.db import models
from django.contrib.auth.forms import User
from django.urls import reverse
from contacts.models import Contact

# Create your models here.

class Meeting(models.Model):
    date = models.DateField()
    time = models.TimeField()
    title = models.TextField(max_length=500)
    location = models.TextField(max_length=200)
    report = models.TextField(
        max_length=2000, 
        null=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        null=True
    )


    #REDIRECTS ON CONTACT CREATION
    def get_absolute_url(self):
        return reverse('meetings:meeting_details', kwargs={'pk': self.pk})

    #OVERRIDE SAVE METHOD to set default Meeting title if not provided
    def save(self, *args, **kwargs):
        if not self.title:
            self.title = "Meeting with {} {} on {}".format(self.contact.first_name, self.contact.last_name, 
            self.date) 
        super(Meeting, self).save(*args, **kwargs)
    