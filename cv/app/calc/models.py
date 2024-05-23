from django.contrib.auth.models import (AbstractBaseUser, AbstractUser,
                                        BaseUserManager, Group, Permission,
                                        PermissionsMixin)
from django.db import models

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, username, password=None):
        user = self.model(username=username)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

class UserRegular(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')
    
class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.TextField()
    end_date = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    graduation_date = models.TextField()

    def __str__(self):
        return self.degree

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CV(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    additional_information = models.TextField(blank=True)

    def __str__(self):
        return self.full_name
    

class Comment(models.Model):
    name = models.CharField(max_length=100)
    e_mail = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.name
