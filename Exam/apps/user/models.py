from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        
        if len(postData['first_name']) < 3:
            errors["first_name"] = "First name should be at least 3 characters"
        if len(postData['last_name']) < 3:
            errors["last_name"] = "Last name should be at least 3 characters"
        try:
            validate_email(postData['email'])
        except ValidationError:
            print('VALIDATION ERROR')
            errors["email"] = "please enter a valid email"
        
        if postData['password'] != postData['confirmed_pw']:
            errors["password"] = "Passwords must be the same"

        if len(postData['password']) < 8:
            errors["password"] = "Passwords should be at least 8 characters"

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    objects = UserManager()
    created_at = models.TimeField(auto_now=True)
    updated_at = models.TimeField(auto_now=True)
 