from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
import bcrypt

class Validation(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['first_name']) <  2:
            errors['first_name'] = "First name needs to be at least 2 characters."
        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Last name needs to be at least 2 characters."
        if not EMAIL_REGEX.match(post_data['signup_email']):
            errors['signup_email'] = "Invalid email entered."
        if post_data['signup_email'] == User.objects.filter(email=post_data['signup_email']):
            errors['signup_email'] = "Email already registered. Please use login."
        if post_data['signup_password'] != post_data['confirm_signup_password']:
            errors['signup_password'] = "Passwords do not match."
        if len(post_data['signup_password']) < 8:
            errors['signup_password'] = "Password needs to be at least 8 characters."
        return errors

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length = 255)
    photo = models.ImageField(upload_to="city_photos/")
    wide_photo = models.ImageField(upload_to="city_photos/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    birthday = models.DateField()
    gender = models.CharField(max_length=20)
    interests = models.TextField()
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=70)
    photo = models.ImageField(upload_to="profile_pics/", default='profile_pics/defaultprofile.png')
    city = models.ForeignKey(City, related_name="users")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Validation()

class Message(models.Model):
    message = models.TextField()
    sender_users = models.ForeignKey(User, related_name="sent_messages")
    receiver_users = models.ForeignKey(User, related_name="received_messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    when = models.DateTimeField()
    location = models.CharField(max_length=255)
    nsa = models.CharField(max_length=25)
    photo = models.ImageField(upload_to="event_photos/")
    admin = models.ForeignKey(User, default=1, null=True, related_name = "admin_of_event")
    city = models.ForeignKey(City, related_name = "events")
    users = models.ManyToManyField(User, related_name="events")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
