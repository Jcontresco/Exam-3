from django.db import models
from apps.user.models import User
from django.core.exceptions import ValidationError
from django.contrib import messages
from datetime import date

class JobManager(models.Manager):
    def basic_validator(self, postData):
        today = date.today()
        errors = {}

        if len(postData['title']) < 3:
            errors['title'] = 'a job must consist of at least 3 characters'
        if len(postData['description']) < 1:
            errors['description'] = 'Description can not be empty'
        if len(postData['location']) < 1:
            errors['location'] = 'Location must be provided'
        return errors
    

class Jobs(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=40)
    join = models.ManyToManyField(User, related_name="joined_user")
    created_at = models.DateField(auto_now=True, null=True)
    updated_at = models.DateField(auto_now=True,  null=True)
    objects = JobManager()

    def __str__(self):
        return f'JOB: {self.title}. DESCRIPTION: {self.description}'