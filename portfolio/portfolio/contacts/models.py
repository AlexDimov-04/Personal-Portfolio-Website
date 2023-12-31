from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=30)

    last_name = models.CharField(max_length=30)

    email = models.EmailField()

    email_subject = models.CharField(max_length=20)

    message = models.TextField()
    