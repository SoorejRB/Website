from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    e_mail = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.e_mail


class Career(models.Model):
    name = models.CharField(max_length=50)
    e_mail = models.EmailField()
    message = models.TextField()
    resume = models.FileField(upload_to="resumes/")

    def __str__(self):
        return self.e_mail


